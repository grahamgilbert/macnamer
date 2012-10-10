from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#import datetime
# Create your models here.
class ComputerGroup(models.Model):
    name = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200, verbose_name="Computer Name Prefix",blank=True,null=True)
    domain = models.CharField(max_length=200, verbose_name="Computer Domain",blank=True,null=True)
    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return self.id

class Computer(models.Model):
    computergroup = models.ForeignKey(ComputerGroup)
    name = models.CharField(max_length=200, verbose_name="Computer Name")
    serial = models.CharField(max_length=200, verbose_name="Serial Number", unique=True)
    last_checkin = models.DateTimeField(blank=True,null=True)