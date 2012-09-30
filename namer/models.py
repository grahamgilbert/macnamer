from django.db import models
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
#import datetime
# Create your models here.
class ComputerGroup(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return self.id
 
    
class Prefix(models.Model):
    prefix = models.CharField(max_length=200, verbose_name="Computer Name Prefix",blank=True,null=True)
    computer_group = models.ForeignKey(ComputerGroup)
    def __unicode__(self):
        return self.prefix
        
def create_prefix(sender, instance, created, **kwargs):
    if created:
        Prefix.objects.create(user=instance)
#only oneprefix per group for now, so this will handle the creating of eachone
post_save.connect(create_prefix, sender=ComputerGroup)

class Computer(models.Model):
    prefix = models.ForeignKey(Prefix)
    name = models.CharField(max_length=200, verbose_name="Computer Name")