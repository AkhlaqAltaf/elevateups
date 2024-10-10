from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core import settings
from src.apps.website.views import WebsiteView

app_name = "website"

urlpatterns = [
    path('', WebsiteView.as_view(), name='portfolio'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)