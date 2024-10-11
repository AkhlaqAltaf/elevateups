from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core import settings
from src.apps.website.views import WebsiteView, BlogDetailView, MoreBlogsView

app_name = "website"

urlpatterns = [
    path('', WebsiteView.as_view(), name='portfolio'),
    path('blog/<int:id>/', BlogDetailView.as_view(), name='blog_detail'),
    path('more-blogs/', MoreBlogsView.as_view(), name='more_blogs'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)