from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from models import *
# Create your views here.
#test

@login_required 
def index(request):
    c = {'user': request.user,}
    return render_to_response('namer/index.html', c) 