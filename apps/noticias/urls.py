
from django.urls import path
from . import views

#LA URL SIEMPRE EMPIEZA CON /Noticias en este archivo, pero solo va a funcionar en la url si su direccion es /Noticias/Listar ya que /Noticias me direcciona a urls de la apps noticias, pero en esta la que me direcciona al html es /Listar

app_name = 'noticias' #aca lo que le digo es que en la url para esta aplicacion se va a llamar noticias

urlpatterns = [
    path('listar/', views.Listar, name = 'listar_noticias'), #el listar/ es solo el string que aparece en la url, el views.Listar es el nombre de la app, y el listar_noticias es como lo vamos a llamar a la vista desde otra vista o pagina

    #PARA MOSTAR EL PATH CON LA VISTA BASADA EN CLASE
    path('detalle/<int:pk>', views.Detalle_Noticia_Clase.as_view(), name = 'detalle_noticia')




    # ASI ES PARA MOSTRAR HACIENDO CON LA FUNCION --> path('detalle/<int:pk>', views.Detalle_Noticia, name = 'detalle_noticia'), #para que me lleve a una determinada noticia tengo que decirle a la url que este preparada para recibir un dato. Entonces va a recibir un entero int que va a recibir una variable que se llama pk. se representa con <> 
    # el pk lo va a recibir la lista en la funcion detalle_noticia como parametro
    #de forma predeterminada django llama pk a la clave primaria
]
