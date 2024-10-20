from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.views.generic import TemplateView

from core import settings
from src.apps.website.views import WebsiteView, BlogDetailView, MoreBlogsView, SiteMap, contact_us_view

app_name = "website"

urlpatterns = [
    path('', WebsiteView.as_view(), name='portfolio'),
    path('blog/<int:id>/', BlogDetailView.as_view(), name='blog_detail'),
    path('more-blogs/', MoreBlogsView.as_view(), name='more_blogs'),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    path('contact/', contact_us_view, name='contact_us'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)