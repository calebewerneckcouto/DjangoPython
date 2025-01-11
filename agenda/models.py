from django.db import models

# Create your models here.
class Categoria(models.Model):  # ORM mapeia alguns atributos dessa classe para banco de dados
    nome = models.CharField(max_length=256,unique=True)   



class Evento(models.Model):
    nome = models.CharField(max_length=256)   
    categoria = models.ForeignKey("Categoria",on_delete=models.SET_NULL,null=True)
    local =  models.CharField(max_length=256,blank=True)   
    link = models.CharField(max_length=256,blank=True)   
    
   # def __init__(self,nome,categoria,local=None,link=None):
   #    self.categoria=categoria
    #    self.local=local
    #    self.link=link
        

     