from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class User_data(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    webpage=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='user',blank=True)

    def __str__(self):
        return self.user.username
    