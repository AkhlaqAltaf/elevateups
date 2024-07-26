"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from calculatorApp import 
# from core import views
admin.site.site_header="Akhlaq Altaf is Admin"
admin.site.site_title="WeCanDo Lab Admin Panel"
admin.site.index_title="Welcome to WeCanDo Lab Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("src.apps.home.urls"),name='home'),
    path('project/', include("src.apps.project.urls"), name='project'),


]
