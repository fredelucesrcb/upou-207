from .views import EmailsView, DiscountsView
from django.urls import path  
  
urlpatterns = [  
    path('basic/', EmailsView.as_view()),  
    path('discount/', DiscountsView.as_view())
]  