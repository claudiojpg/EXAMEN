from django.shortcuts import render, redirect, reverse
from .models import paciente,Genero,medicamento



# Create your views here.
def login_fundap (request):
    context={}
    return render(request,'fundap/login_fundap.html',context)

def home_fundap (request):
    context={}
    return render(request,'fundap/home_fundap.html',context)

def aportes_fundap (request):
    context={}
    return render(request,'fundap/aportes_fundap.html',context)

def datos_fundap(request):
    pacientes = paciente.objects.all()
    context = {"pacientes": pacientes}
    return render(request, 'fundap/datos_fundap.html', context)
def datos_med(request):
    medicamentos= medicamento.objects.all()
    context = {"medicamentos": medicamentos}
    return render(request, 'fundap/medicamentos_fundap.html', context)





def Add_Paciente(request):
    if request.method == 'POST':
        rut = request.POST['txtRut']
        nombre = request.POST['txtNombre']
        apellido_paterno = request.POST['txtApellidoPaterno']
        apellido_materno = request.POST['txtApellidoMaterno']
        fecha_nacimiento = request.POST['txtFechaNacimiento']
        genero_id = request.POST['genero_id']
        telefono = request.POST['txtTelefono']
        informacion_salud = request.POST['txtInformacionSalud']
        activo = request.POST['activo']

        genero = Genero.objects.get(id_genero=genero_id)
        paciente_obj = paciente.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            fecha_nacimiento=fecha_nacimiento,
            id_genero=genero,
            telefono=telefono,
            Informacion_salud=informacion_salud,
            activo=activo
        )

        return redirect(reverse('datos_fundap'))

    generos = Genero.objects.all()
    pacientes = paciente.objects.all()

    context = {
        'generos': generos,
        'pacientes': pacientes
    }

    return render(request, 'fundap/datos_fundap.html', context)