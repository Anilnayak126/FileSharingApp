# views.py

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Folder
from .serializers import FileListSerializer
import os
from django.http import HttpResponse, FileResponse
from django.conf import settings

class FileUploadView(APIView):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        print(request.data)  # For debugging

        serializer = FileListSerializer(data=request.data)
        
        if serializer.is_valid():
            folder_data = serializer.save()
            download_link = request.build_absolute_uri(f"/download/{folder_data['folder']}/")
            return render(request, 'upload.html', {'download_link': download_link})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDownloadView(APIView):
    def get(self, request, folder_uid):
        folder = get_object_or_404(Folder, uid=folder_uid)
        zip_path = f'public/static/zip/{folder.uid}.zip'

        # Check if the zip file exists
        if os.path.exists(zip_path):
            # Serve the download page
            return render(request, 'download.html', {'zip_path': f'{settings.STATIC_URL}zip/{folder.uid}.zip'})
        
        return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)