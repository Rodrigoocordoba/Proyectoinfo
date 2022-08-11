from django.db import models

# Create your models here.

# es como que la clase noticia esta heredando de models.model
#siempre que yo pongo algo en el archivo model debo migrar para que impacte en la bd, esto se hace con python manage.py makemigrations y luego python manage.py migrate
#SIEMPRE QUE MODIFICO EL MODEL DEBO MIGRAR

class Noticia(models.Model): #model.Model siempre va es una clase de django y es el que me transforma la clase noticia en una clase que va a utilizar la ORM de django
    titulo = models.CharField(max_length = 120) #para caracter es models.Charfield(max_length que seria maximo tamaño)
    creado = models.DateField(auto_now_add=True) # el parametro en true es que va a guardar la fecha en la que es modificado o subido automaticamente
    cuerpo = models.TextField() #es para textos largos que no tienen definicion de caracteres, no tiene parametros
    autor = models.CharField(max_length = 50, null = True, blank = True) #es para que me aceptee cuando cargo una noticia en blanco) #el null true es como en base de datos que permite valores nulos, es decir, que no es obligatorio que contenga algo
    imagen = models.ImageField(upload_to = 'noticias', null = True, blank = True) #Lo que le estoy diciendo es que la imagen se guardara en noticias
    
#para las imagenes debemos instalar la libreria pillow, sino no va a funcionar. se instala en el entorno poniendo pip install pillow

    def __str__(self): #debe ir dentro de la clase nombrada, sino no funciona
        return self.titulo# va a mostrar el nombre de los titulos




