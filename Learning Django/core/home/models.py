from django.db import models

from django.db.models.signals import post_save   # import signal
from django.dispatch import receiver

# Create your models here.


class Student(models.Model):
    # id = models.AutoField()  // it automatically generated in schema
    name = models.CharField(max_length=100 )
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    #  image = models.ImageField()
    # file = models.FileField()


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)
    
    def __str__(self) -> str:
        return self.car_name
    


@receiver(post_save, sender=Car)     # it call when above Car object is created
def call_car_api(sender, instance, **kwargs):
    print('\n\nCar object created \n\n')
    print(sender, instance, kwargs)
    