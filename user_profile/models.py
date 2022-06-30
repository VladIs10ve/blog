from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    login = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    surname = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, null=True)
    about = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.name

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
