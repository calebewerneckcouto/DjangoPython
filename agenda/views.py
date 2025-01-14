from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponse,HttpResponseRedirect
from django.template import loader
from agenda.models import Evento
from datetime import date
from django.urls import reverse

# Create your views here.
def listar_eventos(request):
    
    
    eventos = Evento.objects.filter(data__gte=date.today())
    return render(request=request, context={"eventos": eventos}, template_name="agenda/listar_eventos.html")



def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, "agenda/exibir_evento.html", {"evento": evento})


def participar_evento(request):
    evento_id = request.POST.get("evento_id")
    evento = get_object_or_404(Evento,id=evento_id)
    evento.participantes +=1
    evento.save()
    return HttpResponseRedirect(reverse('exibir_evento',args=(evento_id)))
    
    