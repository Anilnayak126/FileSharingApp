import os
import shutil
from rest_framework import serializers
from .models import Folder, Files  # Adjust the import according to your project structure

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False)
    )
    folder = serializers.CharField(required=False)

    def zip_files(self, folder):
        os.makedirs('public/static', exist_ok=True)
        os.makedirs('public/static/zip', exist_ok=True)

        folder_path = os.path.join('public/static', str(folder.uid))  
        zip_path = os.path.join('public/static/zip', str(folder.uid))  

        if os.path.exists(folder_path) and os.listdir(folder_path):
            shutil.make_archive(zip_path, 'zip', folder_path)
        else:
            print('No files to zip in the specified folder.')

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        folder_path = os.path.join('public/static', str(folder.uid))
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            Files.objects.create(folder=folder, file=file)

            # Save file to destination path for zipping later
            destination_path = os.path.join(folder_path, file.name)  
            with open(destination_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

        self.zip_files(folder)
        return {'folder': str(folder.uid)}
