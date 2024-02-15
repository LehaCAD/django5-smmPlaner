from django.db import models

class Post(models.Model):
    file_path = models.FileField(upload_to = 'uploadApp/files/', blank = True)
    description = models.TextField(blank = True)
