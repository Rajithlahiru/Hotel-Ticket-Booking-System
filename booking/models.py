from django.db import models
from datetime import datetime

# Create your models here.
class Booking_detail(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(max_length=50)
    checking_date = models.DateField(default=datetime.now) 
    checkout_date = models.DateField(null=False)
    room = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=15)

    def __str__(self):
        return self.email
