from django.db import models
#from _future_ import unicode_literals
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
#from django.db.models import 0
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
#from rest_framework.authtoken.models import Token
#import validators.UnicodeUsernameValidator


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=73.909)
    lattitude = models.DecimalField(max_digits=8, decimal_places=3, default=25.531)
    phone_regex = RegexValidator(regex=r'^[789]\d{9}$', message="Phone number must be entered in the format: '9999999999'. 10 digits.")
    phone = models.CharField(('phone'), validators=[phone_regex], max_length=10) # validators should be a list
    is_helper = models.BooleanField(default=False)

    
@receiver(post_save, sender= User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender= User)
