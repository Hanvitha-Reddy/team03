"""CS251 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, re_path
    2. Add a URL to urlpatterns:  re_path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from django.views.generic.base import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('accounts.urls', namespace='accounts')),
    re_path('base/', TemplateView.as_view(template_name='base.html'), name='base'),
    re_path(r'^$', RedirectView.as_view(url='/accounts/', permanent=True)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)