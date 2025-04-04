from django.urls import path 
from . import views

urlpatterns = [
    path ('medicos/', views.listagem_medicos, name= 'listagem_medicos'),
    path('consultas/nova/', views.criar_Consultas, name= 'criar_Consultas'),
    path('consultas/<int:pk>/', views.detalhes_consulta, name= 'detalhes_consulta'),
]