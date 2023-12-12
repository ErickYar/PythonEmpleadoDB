from django.db import models

# Crear la clase empleado


class Empleado(models.Model):
    # definir atributos
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    sexo = models.CharField(max_length=15, default='Masculino')
    edad = models.IntegerField()
    fecha = models.DateField()
    sueldo = models.FloatField()

    class Meta:
        db_table = 'Empleado'

    def __str__(self):
        return self.nombre+' '+self.apellidos

# from django.db import models

# # Crear la clase empleado

# class Empleado(models.Model):
#     #definir atributos
#     nombre=models.CharField(max_length=30)
#     apellidos=models.CharField(max_length=30)
#     email=models.EmailField(max_length=60)
#     sexo=models.CharField(max_length=15,default='Masculino')
#     edad=models.IntegerField()
#     fecha=models.DateField()
#     sueldo=models.FloatField()

#     class Meta:
#         db_table='Empleado'

#     def __str__(self):
#         return self.nombre+' '+self.apellidos

