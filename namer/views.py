from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext, Template, Context
from django.template.loader import get_template
from django.core.context_processors import csrf
from models import *
from forms import *
from django.db.models import Q, Max
from datetime import datetime
from django.utils import simplejson
import re

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def next_name(group):
    # Start at 1, try to get a computer. If we fail, then the number is available.
    counter = 1
    if group.prefix:
        while True:
            try:
                computer = get_object_or_404(Computer, name=counter, computergroup=group.id)
                counter += 1
            except Http404:
                break
        return_name = counter
    else:
        return_name = ""

    return return_name

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
        initial_name = next_name(group)
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

#new network
@login_required
@permission_required('namer.add_network', login_url='/login/')
def new_network(request, group_id):
    group = get_object_or_404(ComputerGroup, pk=group_id)
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = NetworkForm(request.POST)
        if form.is_valid():
            the_network = form.save(commit=False)
            the_network.computergroup = group
            the_network.save()
            return redirect('namer.views.show_network', group.id)
    else:
        form = NetworkForm()
    c = {'form': form, 'group':group, }
    return render_to_response('forms/new_network.html', c, context_instance=RequestContext(request))

#edit network
@login_required
@permission_required('namer.change_network', login_url='/login/')
def edit_network(request, network_id):
    network = get_object_or_404(Network, pk=network_id)

    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = NetworkForm(request.POST, instance=network)
        if form.is_valid():
            the_network = form.save(commit=False)
            the_network.save()
            return redirect('namer.views.show_network', network.computergroup.id)
    else:
        form = NetworkForm(instance=network)
    c = {'form': form, 'group':network.computergroup, 'network':network, }
    return render_to_response('forms/edit_network.html', c, context_instance=RequestContext(request))

#show network
@login_required
def show_network(request, group_id):
    group = get_object_or_404(ComputerGroup, pk=group_id)
    networks = group.network_set.all()
    c = { 'user': request.user, 'group':group, 'networks':networks, }
    return render_to_response('namer/show_network.html', c, context_instance=RequestContext(request))

@login_required
@permission_required('namer.delete_network', login_url='/login/')
def delete_network(request, network_id):
    network = get_object_or_404(Network, pk=network_id)
    group = get_object_or_404(ComputerGroup, pk=network.computergroup.id)
    network.delete()
    return redirect('namer.views.show_network', group_id=group.id)

@csrf_exempt
def checkin(request):
    try:
        serial_num = request.POST['serial']
    except:
        raise Http404
    try:
        ip = request.POST['ip']
    except:
        raise Http404

    try:
        key = request.POST['key']
    except:
        raise Http404
    try:
        #try to find the computer
        computer = get_object_or_404(Computer, serial__iexact=serial_num)
    except:
        wan_ip = get_client_ip(request)
        ##we couldn't find the computer, get it's subnet out of the passed ip
        subnet = ip.rpartition('.')[0] + ".0"
        ##find if there are any subnets with this IP address
        try:
            computergroup = get_object_or_404(ComputerGroup, key=key)
        except:
            raise Http404
        ##get the next name of from the group - if it's not blank carry on
        new_name = next_name(computergroup)
        if new_name == "":
            raise Http404
        else:
            ##if there are, create a new computer in that group with the serial
            computer = Computer(name=new_name, serial=serial_num, computergroup=computergroup)
            computer.save()
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
