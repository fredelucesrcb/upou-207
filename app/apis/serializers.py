from rest_framework import serializers  
from .models import (Email, Redemptions_count, Order, Redemption)
  
class EmailSerializer(serializers.ModelSerializer):  
    email = serializers.CharField(max_length=200, required=True)
    code = serializers.CharField(max_length=200, required=False)

    class Meta:  
        model = Email  
        fields = ('__all__')  

    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Email.objects.create(**validated_data)  

class RedemptionsCountSerializer(serializers.ModelSerializer):  
    redemptions_count = serializers.IntegerField(required=True)  
    email_id = serializers.IntegerField(required=True)  

    class Meta:  
        model = Redemptions_count  
        fields = ('__all__')  

    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Redemptions_count.objects.create(**validated_data)  

class OrderSerializer(serializers.ModelSerializer):  
    name = serializers.CharField(max_length=200, required=True)

    class Meta:  
        model = Order  
        fields = ('__all__')  

    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Order.objects.create(**validated_data)  

class RedemptionSerializer(serializers.ModelSerializer):  
    order_id = redemptions_count = serializers.IntegerField(required=True)  
    code = serializers.CharField(max_length=200, required=True)

    class Meta:  
        model = Order  
        fields = ('__all__')       
     
    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Redemption.objects.create(**validated_data)   