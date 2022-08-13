from django.contrib import admin

# Register your models here.
from . models import Noticia, Categoria #importo desde models la clase noticia

admin.site.register(Noticia) #del sitio admin registrar la app noticia

admin.site.register(Categoria)

#luego de haber hecho el migrate de categoria y creado la tabla debo venir aca al admin para poner manejar eso 

