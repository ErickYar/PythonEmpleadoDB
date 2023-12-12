from django.shortcuts import render, redirect
from .models import Empleado
from .forms import EmpleadoForm

def listar(request):
    empleados = Empleado.objects.all()  # select * from empleado
    contexto = {'empleados': empleados}
    return render(request, 'app/listar.html', contexto)

def agregar(request):
    if request.method=='POST':
        #crear objetos de la clase empleados
        form=EmpleadoForm(request.POST)
        if form.is_valid():
            #grabar datos
            form.save(commit=True) #insert into empleado(,,,,)
            return redirect('listar')
    else:
        form=EmpleadoForm()
    contexto={'form':form}
    return render(request, 'app/agregar.html', contexto)

def editar(request,empleado_id):
    #buscar empleados por id
    empleado=Empleado.objects.get(id=empleado_id) # select * from empleados where id=2
    if request.method=='POST':
        #crear objetos de la clase empleado
        form=EmpleadoForm(request.POST,instance=empleado)
        if form.is_valid():
            #grabar datos
            form.save(commit=True) #update empleado set campo1= value1,,,
            return redirect('listar')
    else:
       #crear objetos de la clase empleado form
       form=EmpleadoForm(instance=empleado)
    contexto={'form':form}
    return render(request, 'app/editar.html', contexto)

def eliminar(request,empleado_id):
    #buscar empleado por id 
    empleado=Empleado.objects.get(id=empleado_id)#select * from empleado where
    # eliminar
    empleado.delete()
    return redirect('listar')