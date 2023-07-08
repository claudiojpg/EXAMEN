from django.urls import path
from . import views
from .views import Del_Noticia
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('base',views.base, name='base'),
    path('home', views.home,name='home'),
    path('contacto', views.contacto,name='contacto'),
    path('mensajes/', views.resultado_formulario, name='mensajes'),
    path('login', views.login,name='login'),
    path('internacional', views.noticias_internacional, name='internacional'),
    path('nacional', views.noticias_nacional, name='nacional'),
    path('espectaculos', views.noticias_espectaculos, name='espectaculos'),
    path('deportes', views.noticias_deportes, name='deportes'),
    path('tecnologia', views.noticias_tecnologia, name='tecnologia'),
    path('lista_noticias', login_required(views.Add_Articulo), name='lista_noticias'),
    path('del_noticia/<str:titulo>/', Del_Noticia, name='del_noticia'),
    path('edit_noticia/<str:titulo>/', views.Edit_Noticia, name='edit_noticia'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('noticia/<str:titulo>/', views.vista_noticia, name='vista_noticia'),
    path('procesar-formulario/', views.procesar_formulario, name='procesar_formulario'),
   
   
   
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   