from django.http import HttpResponse
from django.contrib.auth.models import Permission
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, Template, Context
from django.template.loader import get_template
from django.core.context_processors import csrf
from models import *
from forms import *
from django.db.models import Q, Max
# Create your views here.

@login_required 
def index(request):
    #show table with computer groups
    groups = ComputerGroup.objects.all()
    c = {'user': request.user, 'groups':groups, }
    return render_to_response('namer/index.html', c, context_instance=RequestContext(request)) 
    
    
#new computer group
@login_required
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
def new_computer(request, group_id):
    group = get_object_or_404(ComputerGroup, pk=group_id)
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            the_computer = form.save(commit=False)
            the_computer.computergroup = group
            the_computer.save()
            return redirect('namer.views.show_group', group.id)
    else:
    ##is there a prefix set? If so, get the highest number and add one and pre-populate the form with it.
        if group.prefix:
            maximum_name = group.computer_set.all().order_by('-name')[:1]
            try:
                initial_name = int(maximum_name.name)+1
            except TypeError:
                initial_name = ""
        else:
            initial_name = ""
        form = ComputerForm(initial={'name': initial_name})
    c = {'form': form, 'group':group, 'max_name':maximum_name.name, }
    return render_to_response('forms/new_computer.html', c, context_instance=RequestContext(request))

#edit computer

#show computer group
@login_required
def show_group(request, group_id):
    group = get_object_or_404(ComputerGroup, pk=group_id)
    computers = group.computer_set.all()
    c = { 'user': request.user, 'group':group, 'computers':computers, }
    return render_to_response('namer/show_group.html', c, context_instance=RequestContext(request))