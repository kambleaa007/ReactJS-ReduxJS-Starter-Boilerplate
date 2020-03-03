# -*- coding: utf-8 -*-

from django.conf.urls import *
from .views import *

urlpatterns = [ 
    # Hello, world!    
    # Normally should be a separate api/server but to demonstrate proxy behavior  
    url(r'^healthcheck/$', healthCheck),   
    url(r'^api/v1/todos$', todos),
    url(r'^api/v1/badrequest$', badrequest),
    url(r'^api/v1/weather$', weather),
    url(r'^api/v1/mocks$', mocks),
    url(r'', include('proxy.urls')),
    url(r'', index),
]
