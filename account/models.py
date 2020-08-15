from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages
# Create your models here.
def img_upload_directory(instance, filename):
    return f"profile/{instance.username}/{filename}"

class User(AbstractUser):
    image = models.ImageField(default='media/images/ninja.png', blank=True, upload_to=img_upload_directory)
    mobile_no = models.CharField(max_length=11,default='')
    dob = models.DateField(default='')
    location = models.CharField(max_length=100, default='')


@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.ERROR ,"You hvae successfully logged out")