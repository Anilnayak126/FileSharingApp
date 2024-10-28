from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import HandleFileUpload

urlpatterns = [
    path('handle/', HandleFileUpload.as_view(), name='handle_file_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
