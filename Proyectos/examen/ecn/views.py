from django.shortcuts import render,redirect
from .models import Autor,Categoria,Noticia
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from .forms import userForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test




# Create your views here.

def is_admin(user):
    return user.is_superuser

def base (request):
    context={}
    return render(request,'ecn/base.html',context)

def contacto (request):
    context={}
    return render(request,'ecn/contacto.html',context)

def home (request):
    context={}
    return render(request,'ecn/home.html',context)

@user_passes_test(is_admin, login_url='home')
def lista_noticias(request):
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    return render(request, 'ecn/lista_noticias.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_active:
                if user.is_superuser:
                    return redirect('lista_noticias')  
                else:
                    return redirect('home')  
            else:
                return redirect('home')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return redirect('login')
    else:
        return render(request, 'ecn/login.html')


def busqueda(request):
    query = request.POST.get('search_query')
    busqueda = Noticia.objects.filter(categoria__nombre__icontains=query)
    resultados = []
    
    if busqueda:
        resultados = busqueda
        
    context = {
        'resultados': resultados,
        'query': query
    }
    
    return render(request, 'ecn/busqueda.html', context)


def noticias_internacional(request):
    noticias = Noticia.objects.filter(categoria__nombre='Mundo')
    context = {'noticias': noticias}
    return render(request, 'ecn/noticias_internacional.html', context)

def noticias_nacional(request):
    noticias = Noticia.objects.filter(categoria__nombre='Nacional')
    context = {'noticias': noticias}
    return render(request, 'ecn/noticias_nacional.html', context)

def noticias_espectaculos(request):
    noticias = Noticia.objects.filter(categoria__nombre='Espectaculos')
    context = {'noticias': noticias}
    return render(request, 'ecn/noticias_espectaculos.html', context)

def noticias_deportes(request):
    noticias = Noticia.objects.filter(categoria__nombre='Deportes')
    context = {'noticias': noticias}
    return render(request, 'ecn/noticias_deportes.html', context)

def noticias_tecnologia(request):
    noticias = Noticia.objects.filter(categoria__nombre='Tecnologia')
    context = {'noticias': noticias}
    return render(request, 'ecn/noticias_tecnologia.html', context)

def vista_noticia(request, titulo):
    noticia = get_object_or_404(Noticia, titulo=titulo)
    return render(request, 'ecn/vista_noticia.html', {'noticia': noticia})
#:...........................desde aqui empieza el crud........................................................

@user_passes_test(is_admin, login_url='home')
def Add_Articulo(request):
    if request.method == 'POST':
        titulo = request.POST['txtTitulo']
        contenido = request.POST['txtContenido']
        autor_id = request.POST['autor_id']
        categoria_id = request.POST['categoria_id']

        autor = Autor.objects.get(id=autor_id)
        categoria = Categoria.objects.get(id=categoria_id)

        noticia = Noticia.objects.create(
            titulo=titulo,
            contenido=contenido,
            autor=autor,
            categoria=categoria
        )

        return redirect(reverse('lista_noticias'))

    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    noticias = Noticia.objects.all()

    context = {
        'autores': autores,
        'categorias': categorias,
        'noticias': noticias
    }

    return render(request, 'ecn/lista_noticias.html', context)

  
@user_passes_test(is_admin, login_url='home')
def Del_Noticia(request, titulo):
    noticia = Noticia.objects.get(titulo=titulo)
    noticia.delete()
    messages.success(request, '¡Noticia Eliminada!')
    return redirect(reverse('lista_noticias'))
@user_passes_test(is_admin, login_url='home')
def Edit_Noticia(request, titulo):
    if request.method == 'POST':
        noticia = Noticia.objects.get(titulo=titulo)
        noticia.titulo = request.POST['txtTitulo']
        noticia.contenido = request.POST['txtContenido']
        autor_id = request.POST['autor_id']
        noticia.autor = Autor.objects.get(id=autor_id)
        categoria_id = request.POST['categoria_id']
        noticia.categoria = Categoria.objects.get(id=categoria_id)
        if 'imagen' in request.FILES:
            if noticia.imagen:
                noticia.imagen.delete()

            
            imagen = request.FILES['imagen']
            noticia.imagen.save(imagen.name, imagen)

        noticia.save()
        messages.success(request, '¡Noticia Editada!')
        return redirect('lista_noticias')

    noticia = Noticia.objects.get(titulo=titulo)
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()

    context = {
        'noticia': noticia,
        'autores': autores,
        'categorias': categorias,
    }

    return render(request, 'ecn/editar_noticia.html', context)
def procesar_formulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')
        
       

        return render(request, 'ecn/mensajes.html', {
            'nombre': nombre,
            'correo': correo,
            'telefono': telefono,
            'mensaje': mensaje
        })
    else:
        return render(request, 'formulario.html')

def resultado_formulario(request):
    nombre = request.POST.get('nombre')
    correo = request.POST.get('correo')
    telefono = request.POST.get('telefono')
    mensaje = request.POST.get('mensaje')

    return render(request, 'ecn/mensajes.html', {
        'nombre': nombre,
        'correo': correo,
        'telefono': telefono,
        'mensaje': mensaje
    })