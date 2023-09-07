from django.contrib import admin
from django.urls import path
from home  import views

admin.site.site_header = "Akhlaq Altaf"
admin.site.site_title = " developed by Akhlaq Altaf"
admin.site.index_title = "Portfolio"



urlpatterns = [
    path('',views.portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
    path('worksample',views.worksample,name='worksample'),
    path('djangoProjects',views.djangoProjects,name='djangoProjects'),
]
