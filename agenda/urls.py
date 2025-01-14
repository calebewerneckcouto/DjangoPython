from django.urls import path
from agenda.views import exibir_evento

from agenda.views import listar_eventos

urlpatterns=[
    path("", listar_eventos, name="listar_eventos"),
     path("evento/<int:id>/",exibir_evento)
      
]