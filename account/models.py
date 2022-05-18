from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(default='', upload_to="", blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True, default='unkown user')
    img = models.ImageField()

    def __str__(self):
        return str(self.user.username)