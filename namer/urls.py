from django.conf.urls.defaults import *

urlpatterns = patterns('namer.views',
    #front. page
    url(r'^$', 'index', name='home'),
    #new group
    url(r'^group/new/', 'new_computer_group', name='new_computer_group'),
    #edit group
    url(r'^group/edit/(?P<group_id>.+)/', 'edit_computer_group', name='edit_computer_group'),
    #new computer
    url(r'^computer/new/(?P<group_id>.+)/', 'new_computer', name='new_computer'),
    #edit computer
    url(r'^computer/edit/(?P<computer_id>.+)/', 'edit_computer', name='edit_computer'),
    #delete computer
    url(r'^computer/delete/(?P<computer_id>.+)/', 'delete_computer', name='delete_computer'),
    #new network
    url(r'^network/new/(?P<group_id>.+)/', 'new_network', name='new_network'),
    #edit network
    url(r'^network/edit/(?P<network_id>.+)/', 'edit_network', name='edit_network'),
    #delete network
    url(r'^network/delete/(?P<network_id>.+)/', 'delete_network', name='delete_network'),
    #show network
    url(r'^network/show/(?P<group_id>.+)/', 'show_network', name='show_network'),
    #show group
    url(r'^group/show/(?P<group_id>.+)/', 'show_group', name='show_group'),
    #get json info
    url(r'^checkin/', 'checkin', name='checkin'),
)
