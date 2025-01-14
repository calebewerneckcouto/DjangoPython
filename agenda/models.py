from django.db import models

# Create your models here.
class Categoria(models.Model):  # ORM mapeia alguns atributos dessa classe para banco de dados
    nome = models.CharField(max_length=256,unique=True)   
    
    def __str__(self):
        return f"{self.nome} <{self.id}>"


class Evento(models.Model):
    nome = models.CharField(max_length=256)   
    categoria = models.ForeignKey("Categoria", on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256, blank=True)   
    link = models.CharField(max_length=256, blank=True)   
    data = models.DateField(null=True)

    def __str__(self):
        return f"{self.nome} ({self.categoria.nome if self.categoria else 'Sem Categoria'})"


        

     