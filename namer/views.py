from django.http import HttpResponse
from django.contrib.auth.models import Permission
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, Template, Context
from django.template.loader import get_template
from django.core.context_processors import csrf
from models import *
from forms import *
from django.db.models import Q, Max
from datetime import datetime
from django.utils import simplejson
import re

# Create your views here.

@login_required 
def index(request):
    #show table with computer groups
    groups = ComputerGroup.objects.all()
    c = {'user': request.user, 'groups':groups, }
    return render_to_response('namer/index.html', c, context_instance=RequestContext(request)) 
    
    
#new computer group
@login_required
@permission_required('namer.add_computergroup', login_url='/login/')
def new_computer_group(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = ComputerGroupForm(request.POST)
        if form.is_valid():
            new_computer_group = form.save(commit=False)
            new_computer_group.save()
            return redirect('namer.views.show_group', new_computer_group.id)
    else:
        form = ComputerGroupForm()
    c = {'form': form,}
    return render_to_response('forms/new_computer_group.html', c, context_instance=RequestContext(request))

#edit computer group
@login_required
@permission_required('namer.change_computergroup', login_url='/login/')
def edit_computer_group(request, group_id):
    group = get_object_or_404(ComputerGroup, pk=group_id)
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = ComputerGroupForm(request.POST, instance=group)
        if form.is_valid():
            the_group = form.save()
            return redirect('namer.views.show_group', the_group.id)
    else:
        form = ComputerGroupForm(instance=group)
    c = {'form': form, 'group':group, }
    return render_to_response('forms/edit_computer_group.html', c, context_instance=RequestContext(request))

#new computer
@login_required
@permission_required('namer.add_computer', login_url='/login/')
def new_computer(request, group_id):
    group = get_object_or_404(ComputerGroup, pk=group_id)
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            the_computer = form.save(commit=False)
            ##strip the leading zeroes
            the_computer.name = re.sub("^0+","",the_computer.name)
            the_computer.computergroup = group
            the_computer.save()
            return redirect('namer.views.show_group', group.id)
    else:
    ##is there a prefix set? If so, get the highest number and add one and pre-populate the form with it.
        if group.prefix:
            #maximum_name = Computer.objects.filter(computergroup=group.id).order_by('-name')[:1][0]
            maximum_name = Computer.objects.extra(select={'int_name': 'CAST(name AS INTEGER WHERE group_id=group.id)'},order_by=['-int_name'])[0]
            try:
                initial_name = int(maximum_name.name)+1
            except TypeError:
                initial_name = ""
        else:
            initial_name = ""
        form = ComputerForm(initial={'name': initial_name})
    c = {'form': form, 'group':group, }
    return render_to_response('forms/new_computer.html', c, context_instance=RequestContext(request))

#edit computer
@login_required
@permission_required('namer.change_computer', login_url='/login/')
def edit_computer(request, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            the_computer = form.save(commit=False)
            the_computer.name = re.sub("^0+","",the_computer.name)
            the_computer.save()
            return redirect('namer.views.show_group', computer.computergroup.id)
    else:
        form = ComputerForm(instance=computer)
    c = {'form': form, 'group':computer.computergroup, 'computer':computer, }
    return render_to_response('forms/edit_computer.html', c, context_instance=RequestContext(request))
#show computer group
@login_required
def show_group(request, group_id):
    group = get_object_or_404(ComputerGroup, pk=group_id)
    computers = group.computer_set.all()
    ##need to get the longest number.
    length = 0
    for computer in computers:
        this_length = len(computer.name)
        if this_length > length:
            length = this_length
    c = { 'user': request.user, 'group':group, 'computers':computers, 'length':length, }
    return render_to_response('namer/show_group.html', c, context_instance=RequestContext(request))
    
@login_required
@permission_required('namer.delete_computer', login_url='/login/')
def delete_computer(request, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    group = get_object_or_404(ComputerGroup, pk=computer.computergroup.id)
    computer.delete()
    return redirect('namer.views.show_group', group_id=group.id)
    
def checkin(request, serial_num):
    computer = get_object_or_404(Computer, serial__iexact=serial_num)
    computer.last_checkin = datetime.now()
    computer.save()
    group = computer.computergroup
    
    computers = group.computer_set.all()
    ##need to get the longest number.
    length = 0
    for the_computer in computers:
        this_length = len(the_computer.name)
        if this_length > length:
            length = this_length
    c ={'name':computer.name, 'prefix':group.prefix, 'domain':group.domain, 'length':length, }
    return HttpResponse(simplejson.dumps(c), mimetype="application/json")