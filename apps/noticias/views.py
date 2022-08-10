from django.shortcuts import render

# Create your views here.

def Listar(request):
    return render(request,'noticias/listar_noticias.html') #aca lo que le digo es que el html se va a encontrar dentro de la carpeta noticias y se utiliza / para señalar

    
