from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    # models.CASCADE means if model is created and if that model is deleted then usse releted data bhi delete ho jayenga
    # models.SET_NULL means if model is created and if that model is deleted then usse releted data NULL ho jayenga
    # models.SET_DEFAULT means if model is created and if that model is deleted then usse releted data ko default value set ho jayenga

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL)
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")
    
