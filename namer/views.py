from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from models import *
from forms import *
# Create your views here.
#test

@login_required 
def index(request):
    #show table with computer groups
    c = {'user': request.user,}
    return render_to_response('namer/index.html', c) 
    
    
#new computer group
@login_required
def new_computer_group(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = ComputerGroupForm(request.user, request.POST)
        if form.is_valid():
            new_computer_group = form.save(commit=False)
            new_computer_group.save()
            return redirect('namer.views.show_group', new_computer_group.id)
    else:
        form = ComputerGroupForm(request.user)
        #form.group.queryset = Group.objects.filter(organisation=organisation.id)
    c = {'form': form, 'user': request.user,}
    return render_to_response('forms/new_computer_group.html', c, context_instance=RequestContext(request))

#edit computer group

#new prefix

#edit prefix

#new computer

#edit computer

#show computer group
@login_required
def show_group(request, group_id):
    group = get_object_or_404(ComputerGroup, pk=group_id)
    c = { 'user': request.user, 'group':group }
    return render_to_response('namer/show_group.html', c, context_instance=RequestContext(request))