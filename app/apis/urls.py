from .views import EmailsView  
from django.urls import path  
  
urlpatterns = [  
    path('basic/', EmailsView.as_view())  
]  