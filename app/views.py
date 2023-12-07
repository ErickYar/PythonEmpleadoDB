from django.shortcuts import render
from .models import Empleado
from .forms import EmpleadoForm

# funciones para realizar la persistencia de datos

# def listar(request):
#     empleados=Empleado.objects.all() # select * from empleado
#     contexto={'empleados':empleados}
#     return render (request,'app/listar.html',contexto)

def listar(request):
    empleados = Empleado.objects.all()  # select * from empleado
    contexto = {'empleados': empleados}
    return render(request, 'app/listar.html', contexto)
