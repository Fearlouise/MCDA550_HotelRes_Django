from django.db import models

# Create your models here.
class Hotel(models.Model):
    
    hotel_name = models.CharField(max_length=100, null=False)
    street_number = models.CharField(max_length=10, blank=True, null=True)
    street_name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, null=False)
    province = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    price_per_night = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}, {self.hotel_name}"
