from django.shortcuts import render
from django.http.response import HttpResponse
from agenda.models import eventos
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("Olá Mundo!")


def exibir_evento(request):
    evento= eventos[1]
    #template = loader.get_template("agenda/exibir_evento.html")
    #rendered_templeted = template.render(context={"evento":evento},request=request) #Html
    #return HttpResponse(rendered_templeted)
    return render(request=request,context={"evento":evento},template_name="agenda/exibir_evento.html")