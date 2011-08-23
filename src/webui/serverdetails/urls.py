'''
Created on Aug 18, 2011

@author: mmornati
'''

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('webui.serverdetails.views',
  url(r'^details/(?P<hostname>[\w|\W]+)/(?P<instance_name>[\w|\W]+)/$', 'instanceInventory', name = "mcollective-inventory"),
  #Server Inventory
  url(r'^details/(?P<hostname>[\w|\W]+)/$', 'hostInventory', name = "mcollective-inventory"),
  url(r'^tree/(?P<hostname>[\w|\W]+)/$', 'getDetailsTree', name = "mcollective-inventory"),
)
