from django.shortcuts import render
from django.http.response import HttpResponse
from agenda.models import eventos

# Create your views here.
def index(request):
    return HttpResponse("Olá Mundo!")


def exibir_evento(request):
    evento= eventos[1]
    return HttpResponse(f"""
                        <html><h1>Evento:{evento.nome}</h1>
                        <p>Categoria: {evento.categoria}</p>
                        <p>Local:{evento.local}</p>
                        <p>Link:{evento.link}</p>                  
                        """)