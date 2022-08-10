
from django.urls import path
from . import views

#LA URL SIEMPRE EMPIEZA CON /Noticias en este archivo, pero solo va a funcionar en la url si su direccion es /Noticias/Listar ya que /Noticias me direcciona a urls de la apps noticias, pero en esta la que me direcciona al html es /Listar

app_name = 'noticias' #aca lo que le digo es que en la url para esta aplicacion se va a llamar noticias

urlpatterns = [
    path('listar/', views.Listar, name = 'listar_noticias'), #el listar/ es solo el string que aparece en la url, el views.Listar es el nombre de la app, y el listar_noticias es como lo vamos a llamar a la vista desde otra vista o pagina
    
]
