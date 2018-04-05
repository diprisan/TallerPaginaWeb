from django.db import models
from datetime import datetime
from decimal import *

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Usuarios(models.Model):
    user = models.CharField(max_length=200, default='SOME STRING')
    passw = models.CharField(max_length=200, default='SOME STRING')
    nombre = models.CharField(max_length=200, default='SOME STRING')
    apellido2 = models.CharField(max_length=200, default='SOME STRING')
    correo2 = models.CharField(max_length=200, default='SOME STRING')
    fecha_creacion = models.DateTimeField('date published',default=datetime.now())
    fecha_eliminacion = models.DateTimeField('date published',default=datetime.now())
    estado = models.CharField(max_length=200, default='SOME STRING')
    #pub_date = models.DateTimeField('date published')


class cliente(models.Model):
    nombre = models.CharField(max_length=200, default='SOME STRING')
    nacionalidad = models.CharField(max_length=200, default='SOME STRING')
    anio_nacimiento = models.CharField(max_length=200, default='SOME STRING')

class hotel(models.Model):
    nombre = models.CharField(max_length=200, default='SOME STRING')
    direccion = models.CharField(max_length=200, default='SOME STRING')
    telefono = models.CharField(max_length=200, default='SOME STRING')
    correo = models.CharField(max_length=200, default='SOME STRING')
    estado = models.CharField(max_length=200, default='SOME STRING')

class mapa(models.Model):
    latitud = models.CharField(max_length=200, default='SOME STRING')
    longitud = models.CharField(max_length=200, default='SOME STRING')
    estado = models.CharField(max_length=200, default='SOME STRING')

class galeria(models.Model):
    nombre_foto = models.CharField(max_length=200, default='SOME STRING')
    id_hotel = models.CharField(max_length=200, default='SOME STRING')
    estado = models.CharField(max_length=200, default='SOME STRING')

class tipo_habitacion(models.Model):
    nombre = models.CharField(max_length=200, default='SOME STRING')

class ventas(models.Model):
    numero_factura = models.CharField(max_length=200, default='SOME STRING')
    id_hotel = models.CharField(max_length=200, default='SOME STRING')
    anio = models.CharField(max_length=200, default='SOME STRING')
    mes = models.CharField(max_length=200, default='SOME STRING')
    precio_total = models.CharField(max_length=200, default='SOME STRING')
    cantidad = models.CharField(max_length=200, default='SOME STRING')
    tipo_habitacion = models.CharField(max_length=200, default='SOME STRING')
    id_cliente = models.CharField(max_length=200, default='SOME STRING')

class ventas_totales(models.Model):
    id_hotel = models.IntegerField(default=0)
    anio = models.CharField(max_length=200, default='SOME STRING')
    mes = models.CharField(max_length=200, default='SOME STRING')
    total = models.CharField(max_length=200, default='SOME STRING')
    cant_facturas = models.CharField(max_length=200, default='SOME STRING')
    normal = models.CharField(max_length=200, default='SOME STRING')
    suit = models.CharField(max_length=200, default='SOME STRING')
    salon = models.CharField(max_length=200, default='SOME STRING')
    cliente = models.CharField(max_length=200, default='SOME STRING')
    Italia =  models.CharField(max_length=200, default='SOME STRING')
    Espania =  models.CharField(max_length=200, default='SOME STRING')
    Ecuador =  models.CharField(max_length=200, default='SOME STRING')
    Extranjeros = models.CharField(max_length=200, default='SOME STRING')
    Mexico =  models.CharField(max_length=200, default='SOME STRING')
    Brasil =  models.CharField(max_length=200, default='SOME STRING')
    Peru =  models.CharField(max_length=200, default='SOME STRING')
    Colombia =  models.CharField(max_length=200, default='SOME STRING')
    Venezuela =  models.CharField(max_length=200, default='SOME STRING')

class suma_habitacion(models.Model):
    id_hotel = models.IntegerField(default=0)
    anio = models.IntegerField(default=0)
    mes = models.IntegerField(default=0)
    habitacion = models.CharField(max_length=200, default='SOME STRING')
    numero_facturas = models.IntegerField(default=0)
    total_habitacion = models.IntegerField(default=0)

class nacionalesextranjeros(models.Model):
    id_hotel = models.IntegerField(default=0)
    anio = models.IntegerField(default=0)
    Italia = models.CharField(max_length=200, default='SOME STRING')
    Espania = models.CharField(max_length=200, default='SOME STRING')
    Ecuador = models.CharField(max_length=200, default='SOME STRING')
    Mexico = models.CharField(max_length=200, default='SOME STRING')
    Brasil = models.CharField(max_length=200, default='SOME STRING')
    Peru = models.CharField(max_length=200, default='SOME STRING')
    Colombia = models.CharField(max_length=200, default='SOME STRING')
    Venezuela = models.CharField(max_length=200, default='SOME STRING')
