from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import (Email)  
from .serializers import (EmailSerializer)  
import string
import random
from django.core.mail import send_mail
from django.core.mail import EmailMessage 

from django.template.loader import get_template
from django.template import Context
  
class EmailsView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Email.objects.all()  
        serializers = EmailSerializer(result, many=True) 
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):   
        updated_request = request.POST.copy()
        email_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        email = request.data['email']
        updated_request.update({'email': email ,'code': email_code})
        serializer = EmailSerializer(data=updated_request)

        if serializer.is_valid():  
            serializer.save()  

            message = get_template("body.html").render({
            'email': email,
            'code': email_code
            })

            mail = EmailMessage('Welcome to our newsletter!', body = message, from_email="store@email.com", to=[email])
            mail.content_subtype = "html"
            mail.send()

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  

class DiscountsView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Email.objects.all()  
        serializers = EmailSerializer(result, many=True) 
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):   
        result = Email.objects.filter(code=request.data['code'])

        if result:
            return Response({"status": "success"}, status=status.HTTP_200_OK)  
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)  