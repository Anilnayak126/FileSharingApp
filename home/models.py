

from django.db import models
from uuid import uuid4
import uuid
import os


def get_upload_path(instance, filename):
    # Generates the path using the folder's unique ID
    return os.path.join(str(instance.folder.uid), filename)
class Folder(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)

class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateField(auto_now=True)
