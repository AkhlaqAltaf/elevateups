from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

app_name = "project"
urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
