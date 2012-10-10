from django.conf.urls.defaults import *

urlpatterns = patterns('namer.views',
    #front. page
    url(r'^$', 'index', name='home'),
    #new group
    url(r'^group/new/', 'new_computer_group', name='new_computer_group'),
    #edit group
    url(r'^group/edit/(?P<group_id>.+)/', 'edit_computer_group', name='edit_computer_group'),
    #new comouter
    url(r'^computer/new/(?P<group_id>.+)/', 'new_computer', name='new_computer'),
    #edit computer
    url(r'^computer/edit/(?P<computer_id>.+)/', 'edit_computer', name='edit_computer'),
    #delete computer
    url(r'^computer/delete/(?P<computer_id>.+)/', 'delete_computer', name='delete_computer'),
    #show group
    url(r'^group/show/(?P<group_id>.+)/', 'show_group', name='show_group'),
    #get json info
    url(r'^checkin/(?P<serial_num>.+)/', 'checkin', name='checkin'),
    #url(r'^new$', 'new'),
    #url(r'^delete/(?P<manifest_name>[^/]+)/$', 'delete'),
    #url(r'^#(?P<manifest_name>.+)/$', 'index'),
    #url(r'^view/(?P<manifest_name>[^/]+)/$', 'view'),
)
