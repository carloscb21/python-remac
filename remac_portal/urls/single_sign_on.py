#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Event SSO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete

from remac_portal.views.portal import RegisterView, ChangePasswordView

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'portal/single_sign_on/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'portal/single_sign_on/logout.html'}, name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),

    url(r'^change-password/$', ChangePasswordView.as_view(), name='change_password'),

    url(r'^reset-password/$', password_reset,
        {'template_name': 'portal/single_sign_on/reset_password.html', 'post_reset_redirect': 'user:password_reset_done',
         'email_template_name': 'portal/single_sign_on/reset_password_email.html'}, name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done,
        {'template_name': 'portal/single_sign_on/reset_password_done.html'}, name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'portal/single_sign_on/reset_password_confirm.html',
         'post_reset_redirect': 'user:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete,
        {'template_name': 'portal/single_sign_on/reset_password_complete.html'}, name='password_reset_complete')

]
