from django.shortcuts import render, redirect, get_object_or_404
from .models import RESERVACION, SHOW
from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def inicio(request):
    return render(request, 'index.html')

def listar_reservaciones(request):
    reservaciones = RESERVACION.objects.all()
    return render(request, 'listar.html', {'reservaciones': reservaciones})

def listar_empleado(request):
    reservaciones = RESERVACION.objects.all()
    return render(request, 'listar_empleado.html', {'reservaciones': reservaciones})

def crear_reservacion(request):
    if request.method == 'POST':
        nombre_cliente = request.POST['txtNombre_Cliente']
        fecha_evento = request.POST['txtFecha']
        num_invitados = request.POST['txtNum_Inv']
        tipo_evento = request.POST['txtTipo_Evento']
        telefono_contacto = request.POST['txtTelefono_Contacto']
        estatus = request.POST['ddlestatus']

        RESERVACION.objects.create(nombre_cliente=nombre_cliente, fecha_evento=fecha_evento, num_invitados=num_invitados, tipo_evento=tipo_evento, telefono_contacto=telefono_contacto, estatus=estatus)
        return redirect('listar')
    return render(request, 'crear.html')

def editar_reservacion(request, id):
    reservacion = get_object_or_404(RESERVACION, id=id)
    if request.method == 'POST':
        reservacion.nombre_cliente = request.POST['txtNombre_Cliente']
        reservacion.fecha_evento = request.POST['txtFecha']
        reservacion.num_invitados = request.POST['txtNum_Inv']
        reservacion.tipo_evento = request.POST['txtTipo_Evento']
        reservacion.telefono_contacto = request.POST['txtTelefono_Contacto']
        reservacion.estatus = request.POST['ddlestatus']

        reservacion.save()
        return redirect('listar')
    return render(request, 'editar.html', {'reservacion': reservacion})

def eliminar_reservicion(request, id):
    reservacion = get_object_or_404(RESERVACION, id=id)
    reservacion.delete()
    return redirect('listar')

class RoleLoginForm(AuthenticationForm):
    role = forms.ChoiceField(
        choices=[('admin', 'Administrador'), ('empleado', 'Empleado')],
        label='Tipo de usuario'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget.attrs.update({'id': 'id_role'})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = RoleLoginForm

    def form_valid(self, form):
        role = self.request.POST.get('role')
        if role == 'admin':
            return redirect('listar')
        else:
            return redirect('listar_empleado')
        
def marcar_listo(request, id):
    reservacion = get_object_or_404(RESERVACION, id=id)
    reservacion.estatus = "listo"
    reservacion.save()
    return redirect('listar_empleado')