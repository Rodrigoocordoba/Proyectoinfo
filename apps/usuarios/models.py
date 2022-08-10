from django.db import models

# Create your models here.
#aca van a estar los modelos que van a impactar en la base de datos 

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    pass