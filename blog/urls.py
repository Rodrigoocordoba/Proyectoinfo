"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views #de la misma carpeta en la que estoy importar el archivo views
urlpatterns = [
    path('admin/', admin.site.urls),
    #URL PRINCIPAL
    path('',views.Home, name = 'home'), #url para el home, significa que si viene vacio '' entonces me direcciona hacia el home

    #URL DE APLICACIONES
    path('Noticias/',include('apps.noticias.urls')), # siempre que venga en el url noticias me redirecciona hacia mi apps de noticias
]
