from django.db import models
from django.utils import timezone

class Students(models.Model):  
    first_name = models.CharField(max_length=200)  
    last_name = models.CharField(max_length=200)  
    address = models.CharField(max_length=200)  
    roll_number = models.IntegerField()  
    mobile = models.CharField(max_length=10)  
  
    def __str__(self):  
        return self.first_name + " " + self.last_name  

class Email(models.Model):  
    email = models.CharField(max_length=200, unique=True)  
    code = models.CharField(max_length=200)  
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Redemptions_count(models.Model):  
    redemptions_count = models.IntegerField()
    email_id = models.ForeignKey(Email, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Order(models.Model):  
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Redemption(models.Model):  
    order_id= models.ForeignKey(Order, on_delete=models.CASCADE)
    code = models.CharField(max_length=200) 
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

