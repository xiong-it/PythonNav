from django.conf.urls import patterns, include, url

import xadmin
from sso_server.views import *

#from django.contrib.auth.views import


urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^admin/', include(xadmin.site.urls)),
                       # url(r'^server/', include(sso_server.get_urls())),
                       # url(r'^login/$', 'sso_server.views.login', {'template_name': 'login.html'}, name='login'),
                       # url(r'^logout/$', 'sso_server.views.logout_view', name='logout'),
                       # url(r'^chpw/$','sso_server.views.chpw',name='chpw'),
                       #url(r'^forgotpwd/$','sso_server.views.forgot_passwd',name='forgotpwd'),
                       )

