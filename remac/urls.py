"""remac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from remac_portal.views.portal import login_redirect
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',  login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('remac_portal.urls.portal', namespace='portal')),
    url(r'^apis/', include('remac_portal.urls.apis', namespace='apis')),
    url(r'^backoffice/', include('remac_portal.urls.backoffice', namespace='backoffice')),
    url(r'^user/', include('remac_portal.urls.single_sign_on', namespace='user')),  # CAS Client #Checked

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


