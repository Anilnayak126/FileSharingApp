from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import FileUploadView, FileDownloadView

urlpatterns = [
    path('', FileUploadView.as_view(), name='file-upload'),
    path('download/<uuid:folder_uid>/', FileDownloadView.as_view(), name='file-download'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

