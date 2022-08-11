from django.contrib import admin

# Register your models here.
from . models import Noticia #importo desde models la clase noticia

admin.site.register(Noticia) #del sitio admin registrar la app noticia

