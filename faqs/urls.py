
from django.urls import path,include
from .views import *;

urlpatterns = [
  
    path('faqs/',FAQview.as_view(),name="faq-list")
   
]