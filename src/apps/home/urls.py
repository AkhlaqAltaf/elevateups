from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core import settings
from src.apps.home import views

admin.site.site_header = "Akhlaq Altaf"
admin.site.site_title = " developed by Akhlaq Altaf"
admin.site.index_title = "Portfolio"



urlpatterns = [
    path('', views.HomePageView.as_view(), name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('worksample', views.worksample, name='worksample'),
    path('djangoProjects', views.djangoProjects, name='djangoProjects'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)