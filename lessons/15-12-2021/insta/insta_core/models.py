from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ava = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='post text')
    image = models.ImageField(verbose_name='post image')

    def __str__(self):
        return f"({self.user.username}) {self.text[0:30]}"
