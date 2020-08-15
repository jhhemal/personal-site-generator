from django.db import models
from account.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
# Create your models here.



class Website(models.Model):

    TEMPLATE_CHOICES = (
        ('default', 'default'),
        ('template2', 'template2'),
        ('template3', 'template3'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, default="")
    bio = models.TextField(verbose_name="Enter Your bio", null=True, blank=True)
    template = models.CharField(verbose_name="Select Template",max_length=15, choices=TEMPLATE_CHOICES, default='default', blank=True)
    facebook = models.CharField(max_length=50, default="", blank=True)
    twitter = models.CharField(max_length=50, default="", blank=True)
    linkedin = models.CharField(max_length=50, default="", blank=True)
    github = models.CharField(max_length=50, default="", blank=True)
    instagram = models.CharField(max_length=50, default="", blank=True)
    cv_link = models.CharField(max_length=200, default="", blank=True)
    

class Skill(models.Model):
    title = models.CharField(max_length=50)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Interest(models.Model):
    title = models.CharField(max_length=50)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Badge(models.Model):
    title = models.CharField(verbose_name='Badge Title', max_length=20)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Education(models.Model):
    YEAR_CHOICES = []
    for r in range(1950, (datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    name = models.CharField(max_length=100)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    yrfrom = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    yrto = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)



@receiver(post_save, sender=User)
def create_user_website(sender, instance, created, **kwargs):
    if created:
        Website.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_website(sender, instance, **kwargs):
    instance.website.save()
