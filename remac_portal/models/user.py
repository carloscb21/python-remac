from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib import admin


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
admin.site.register(UserProfile)