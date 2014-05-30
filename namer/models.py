from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import random
import string
#import datetime
# Create your models here.
def GenerateKey():
    key = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(128))
    try:
        ComputerGroup.objects.get(key=key)
        return GenerateKey()
    except ComputerGroup.DoesNotExist:
        return key;
class ComputerGroup(models.Model):
    name = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200, verbose_name="Computer Name Prefix",blank=True,null=True)
    domain = models.CharField(max_length=200, verbose_name="Computer Domain",blank=True,null=True)
    key = models.CharField(max_length=255, unique=True, blank=True, null=True)
    def save(self):
        if not self.id:
            self.key = GenerateKey()
        super(ComputerGroup, self).save()
    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return self.id

class Network(models.Model):
    network = models.CharField(max_length=200, unique=True)
    computergroup = models.ForeignKey(ComputerGroup)
    def __unicode__(self):
        return self.network
    class Meta:
        ordering = ['network']

class Computer(models.Model):
    computergroup = models.ForeignKey(ComputerGroup)
    name = models.CharField(max_length=200, verbose_name="Computer Name")
    serial = models.CharField(max_length=200, verbose_name="Serial Number", unique=True)
    last_checkin = models.DateTimeField(blank=True,null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
