from django.shortcuts import render

from . models import Noticia #siempre debo importar
# Create your views here.

def Listar(request):
    #Para mostrar las noticias en la pagina se crea un diccionario que se lo encuentra comunmente llamado como contexto (ctx)
    ctx = {} #creo el diccionario para pasar datos al template
    #BUSCO LO QUE QUIERO EN LA BD
    todas = Noticia.objects.all()
    print(todas) #para saber que lo de arriba anda hacemos un print
    #PASARLO AL TEMPLATE
    ctx['notis'] = todas
    return render(request,'noticias/listar_noticias.html', ctx, ) #aca lo que le digo es que el html se va a encontrar dentro de la carpeta noticias y se utiliza / para señalar









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
