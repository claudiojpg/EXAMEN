from django.urls import path
from . import views



urlpatterns = [
    path('home_fundap', views.home_fundap, name='home_fundap'),
    path('login_fundap', views.login_fundap, name='login_fundap'),
    path('aportes_fundap', views.aportes_fundap, name='aportes_fundap'),
    path('datos_fundap', views.Add_Paciente, name='datos_fundap'),
    path('medicamentos_fundap',views.datos_med,name='medicamentos_fundap'),
      
]