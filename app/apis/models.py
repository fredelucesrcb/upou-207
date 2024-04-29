from django.db import models


class Students(models.Model):  
    first_name = models.CharField(max_length=200)  
    last_name = models.CharField(max_length=200)  
    address = models.CharField(max_length=200)  
    roll_number = models.IntegerField()  
    mobile = models.CharField(max_length=10)  
  
    def __str__(self):  
        return self.first_name + " " + self.last_name  

class Email(models.Model):  
    email = models.CharField(max_length=200)  
    code = models.CharField(max_length=200)  
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

class Redemptions_count(models.Model):  
    redemptions_count = models.IntegerField()
    email_id = models.ForeignKey(Email, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

class Order(models.Model):  
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

class Redemption(models.Model):  
    order_id= models.ForeignKey(Order, on_delete=models.CASCADE)
    code = models.CharField(max_length=200) 
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

