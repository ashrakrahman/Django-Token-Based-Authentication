from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Product (models.Model):
    product_name = models.CharField(max_length=255,default="")
    product_description = models.CharField(max_length=1000,default="")
    product_price = models.IntegerField(default=0)
    company_name =  models.CharField(max_length=255, default="")
    company_country = models.CharField(max_length=255,default="")
    product_bid = models.IntegerField(default=0)


    def __str__(self):
        return self.product_name
