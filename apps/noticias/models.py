from django.db import models

# Create your models here.

# es como que la clase noticia esta heredando de models.model
#siempre que yo pongo algo en el archivo model debo migrar para que impacte en la bd, esto se hace con python manage.py makemigrations y luego python manage.py migrate


#-------> SIEMPRE QUE MODIFICO EL MODEL DEBO MIGRAR   <---------------------

#PARA QUE UN TIPO DE DATO SEA DESPLEGABLE Y EVITAR TIPOS DE ERRORES, COMO EN ESTE CASO CATEGORIA, LO QUE DEBEMOS HACER ES HACERLO UNA CLASE

class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=250, null=True, blank = True)

    def __str__(self):
        return self.nombre


class Noticia(models.Model): #model.Model siempre va es una clase de django y es el que me transforma la clase noticia en una clase que va a utilizar la ORM de django
    titulo = models.CharField(max_length = 120) #para caracter es models.Charfield(max_length que seria maximo tamaño)
    creado = models.DateField(auto_now_add=True) # el parametro en true es que va a guardar la fecha en la que es modificado o subido automaticamente
    cuerpo = models.TextField() #es para textos largos que no tienen definicion de caracteres, no tiene parametros
    autor = models.CharField(max_length = 50, null = True, blank = True) #es para que me aceptee cuando cargo una noticia en blanco) #el null true es como en base de datos que permite valores nulos, es decir, que no es obligatorio que contenga algo
    imagen = models.ImageField(upload_to = 'noticias', null = True, blank = True) #Lo que le estoy diciendo es que la imagen se guardara en noticias
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, null=True) #ACA LA RELACION SERIA QUE UNA RELACION PERTENECE A UNA CATEGORIA Y UNA CATEGORIA PUEDE ESTAR EN MUCHAS NOTICIAS, ENTONCES LA FOREINGKEY VA EN NOTICIAS
    #categoria dice que la noticia va a tener un campo categoria que va a ser una clave foranea a la clase categoria y el on delete significa que pasa si borro la categoria, ES DECIR QUE SI BORRO UN TIPO DE CATEGORIA SE VAN A BORRAR TODAS LAS NOTICIAS ASOCIADAS A ESA
    #cuando hago el migrations de categoria salta un error porque ya tengo noticias cargadas y no tengo categorias todavia, entonces debo agregar el null true, sino no hay forma
    #generalmente las claves foraneas se ponen al empezar el trabajo y sino la unica solucion es poner que sean nulas
    #y si da un error por haber cargado la migracion sin el null lo que se debe hacer es borrar la ultima migracion de la carpeta migrations 
#para las imagenes debemos instalar la libreria pillow, sino no va a funcionar. se instala en el entorno poniendo pip install pillow

    def __str__(self): #debe ir dentro de la clase nombrada, sino no funciona
        return self.titulo # va a mostrar el nombre de los titulos




