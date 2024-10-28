import shutil
from rest_framework import serializers
from .models import Folder, Files
import os

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False)
    )
    folder = serializers.CharField(required=False)

    def zip_files(self, folder):
        folder_path = os.path.join('public/static', str(folder.uid))  # Adjusted path
        zip_path = os.path.join('public/static/zip', str(folder.uid))  # Adjusted path for the zip file
        shutil.make_archive(zip_path, 'zip', folder_path)

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []

        for file in files:
            files_obj = Files.objects.create(folder=folder, file=file)
            files_objs.append(files_obj)

         # Call to create the zip file
        return {'files': {}, 'folder': str(folder.uid)}
