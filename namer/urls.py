from django.conf.urls.defaults import *

urlpatterns = patterns('namer.views',
    #front. page
    url(r'^$', 'index'),
    #new group
    url(r'^group/new/', 'new_computer_group', name='new_computer_group'),
    #new prefix
    #edit group
    #edit prefix
    #new comouter
    #edit computer
    #show group
    url(r'^group/show/(?P<group_id>.+)/', 'show_group', name='show_group'),
    #show computer
    #get json info
    #url(r'^new$', 'new'),
    #url(r'^delete/(?P<manifest_name>[^/]+)/$', 'delete'),
    #url(r'^#(?P<manifest_name>.+)/$', 'index'),
    #url(r'^view/(?P<manifest_name>[^/]+)/$', 'view'),
)
