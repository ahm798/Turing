from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(default='', upload_to="", blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True, default='TEST')
    socials = models.ManyToManyField('Social', blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    verified  = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)



