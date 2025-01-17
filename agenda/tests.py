from django.test import TestCase,Client
from agenda.models import Evento,Categoria
from datetime import date


# Create your tests here.

class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response=client.get("/")
       #self.assertContains(response,"<th>Nome</th>") # verifica se a pagina esta renderizando isso /se tiver e pq esta funcionando...
        self.assertTemplateUsed(response,"agenda/listar_eventos.html") # verifica se esta renderizando o template certo
 
 
class TestListagemDeEventos(TestCase):
    def test_evento_com_data_de_hoje_e_exibido(self):  
        categoria = Categoria()
        categoria.name="Machine Learning"
        categoria.save()
             
        evento = Evento()
        evento.nome="Aula de Inteligencia Artificial"
        evento.categoria =categoria
        evento.local="Santa Catarina"
        evento.data=date.today()
        evento.save()
        
        client = Client()
        response=client.get("/")
        self.assertContains(response,"Aula de Inteligencia Artificial")
        self.assertContains(response,"A Definir")
        self.assertEqual(response.context["eventos"][0],evento)