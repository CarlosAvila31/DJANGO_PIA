from django.shortcuts import render, redirect, get_object_or_404
from .models import RESERVACION, SHOW

# Create your views here.


def inicio(request):
    return render(request, 'index.html')

def listar_reservaciones(request):
    reservaciones = RESERVACION.objects.all()
    return render(request, 'listar.html', {'reservaciones': reservaciones})

def crear_reservacion(request):
    if request.method == 'POST':
        nombre_cliente = request.POST['nombre_cliente']
        fecha_evento = request.POST['fecha_evento']
        num_invitados = request.POST['num_invitados']
        tipo_evento = request.POST['tipo_evento']
        telefono_contacto = request.POST['telefono_contacto']
        estatus = request.POST['estatus']

        RESERVACION.objects.create(nombre_cliente=nombre_cliente, fecha_evento=fecha_evento, num_invitados=num_invitados, tipo_evento=tipo_evento, telefono_contacto=telefono_contacto, estatus=estatus)
        return redirect('listar')
    return render(request, 'crear.html')

def editar_reservacion(request, id):
    reservacion = get_object_or_404(RESERVACION, id=id)
    if request.method == 'POST':
        reservacion.nombre_cliente = request.POST['nombre_cliente']
        reservacion.fecha_evento = request.POST['fecha_evento']
        reservacion.num_invitados = request.POST['num_invitados']
        reservacion.tipo_evento = request.POST['tipo_evento']
        reservacion.telefono_contacto = request.POST['telefono_contacto']
        reservacion.estatus = request.POST['estatus']

        reservacion.save()
        return redirect('listar')
    return render(request, 'editar.html', {'reservacion': reservacion})

def eliminar_reservicion(request, id):
    reservacion = get_object_or_404(RESERVACION, id=id)
    reservacion.delete()
    return redirect('listar')