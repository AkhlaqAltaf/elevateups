from django.contrib import admin
from django.urls import path

from src.apps.website.views import WebsiteView

app_name = "website"

urlpatterns = [
    path('', WebsiteView.as_view(), name='portfolio'),

]
