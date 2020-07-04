"""yourquery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from accounts.views import (login_view, 
                            register_view, 
                            logout_view, 
                            user_profile, 
                            user_profile_update)
from contact.views import contact
from core.views import home, about,blog,visitblog,addblog
from django.urls import re_path,path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    #Core
    re_path(r'^$', home, name='home'),
    re_path(r'^about/$', about, name='about'),
    re_path(r'^blog/$', blog,name='blog'),
    path('visitblog/<int:id>/', visitblog,name='visitblog'),
    path('addblog/', addblog,name='addblog'),
    #Accounts
    re_path(r'^profile/(?P<username>\w+)/$', user_profile, name='user_profile'),
    re_path(r'^profile/(?P<username>\w+)/edit/$', user_profile_update, name='user_profile_update'),
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^register/$', register_view, name='register'),
    re_path(r'^logout/$', logout_view, name='logout'),
    #Contact
    re_path(r'^contact/$', contact, name='contact'),
    #Questions
    re_path(r'^questions/', include('questions.urls', namespace='questions')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
