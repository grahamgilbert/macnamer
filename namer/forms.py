from django import forms
from models import *

class ComputerGroupForm(forms.ModelForm):
    class Meta:
        model = ComputerGroup
        fields = ('name','prefix','domain',)

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('name','serial',)
        
class NetworkForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = ('network',)