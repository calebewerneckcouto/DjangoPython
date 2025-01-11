from django.urls import path
from agenda.views import index
from agenda.views import soma

urlpatterns=[
     path("",index),
      
]