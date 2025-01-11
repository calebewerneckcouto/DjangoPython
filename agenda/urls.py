from django.urls import path
from agenda.views import index

from agenda.views import exibir_evento

urlpatterns=[
     path("",index),
     path("evento",exibir_evento)
      
]