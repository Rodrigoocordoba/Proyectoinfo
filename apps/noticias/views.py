from django.shortcuts import render

#importo las librerias para hacer la vista basada en clase
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from . models import Noticia #siempre debo importar
# Create your views here.

def Listar(request): #VISTA BASADA EN FUNCIONES
    #Para mostrar las noticias en la pagina se crea un diccionario que se lo encuentra comunmente llamado como contexto (ctx)
    ctx = {} #creo el diccionario para pasar datos al template
    #BUSCO LO QUE QUIERO EN LA BD
    todas = Noticia.objects.all()
    print(todas) #para saber que lo de arriba anda hacemos un print
    #PASARLO AL TEMPLATE
    ctx['notis'] = todas
    return render(request,'noticias/listar_noticias.html', ctx) #aca lo que le digo es que el html se va a encontrar dentro de la carpeta noticias y se utiliza / para señalar

#parte de traer las noticias o datos de la bd como lo hacemos nosotros, url luego vista y luego el template. Existe algo que se llama vistas basadas en clases 

class Detalle_Noticia_Clase(DetailView): #VISTA BASADA EN CLASE
    model = Noticia
    template_name = 'noticias/detalle_noticia.html'
#SI USO UNA VISTA BASADA EN CLASE EL CONTEXTO SE LE LLAMA:
#SI ES UNO SOLO object
#SI SON MUCHOS SE LLAMA object_list



''' ASI MOSTRARIA EL DETALLE DE CADA NOTICIA, PERO VOY A PROBAR HACIENDO CON LA VISTA BASADA EN CLASE
def Detalle_Noticia(request, pk):
    #una vez que tengo esa pk tengo que capturarla en un diccionario como ya hicimos en listar y pasarla a detalle noticia
    ctx = {}
    noticia = Noticia.objects.get(pk = pk) #aca coincide que los dos se llaman pk pero a la variable que nosotros la llamamos asi podemos cambiarla
    ctx['resultado'] = noticia
    return render(request,'noticias/detalle_noticia.html',ctx )'''





''' PARA QUE ME TRAIGA TODAS LAS NOTICIAS SE HACE A TRAVES DE LA ORM

Los tipos de consulta que vamos a usar son:

Nombre.Modelo.objects.get(id = myID) --> se usa si estoy seguro que el resultado es un solo objeto, es decir filtra por clave, el resultado va a ser un solo registro

Nombre.Modelo.objects.filter(campo1 = myfiltro1, campo2 = myfiltro2)  -->  este lo que hace es traerme todos los que sean iguales

Nombre.Modelo.objects.all()  --> este seria un select*from'''


#EJEMPLO DE COMO DESARMA EL CTX EL TEMPLATE
#ctx['nombre'] = 'nicolas'
#ctx['notas'] = [5,6,9]
#EL TEMPLATE ya separa el diccionario
#nombre = 'nicolas'
#notas = [5,6,9]
