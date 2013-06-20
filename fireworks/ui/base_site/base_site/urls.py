__author__ = 'Morgan Hargrove'
__copyright__ = 'Copyright 2013, The Materials Project'
__version__ = '0.1'
__maintainer__ = 'Morgan Hargrove'
__email__ = 'mhargrove@lbl.gov'
__date__ = 'Jun 13, 2013'

from django.conf.urls import patterns, include, url
from base_site.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # home index page
    ('^$', home),
    # url(r'^base_site/', include('base_site.foo.urls')),

    # FireWorks index
    ('^fw/$', fw),
    # FireWork info pages
    (r'^fw/(\d+)/$', fw_id),
    # (r'^fw/(\d+)/(more|less|all)/$', fw),

    # WorkFlows index
    ('^wf/$', wf),
    # WorkFlow info pages
    (r'^wf/(\d+)/$', wf_id),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
