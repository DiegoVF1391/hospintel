from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_image, name='upload'),
    #Vistas para el paciente
    path('paciente/', views.paciente_list, name='paciente_list'),
    path('paciente/create/', views.paciente_create, name='paciente_create'),
    path('paciente/<int:pk>/', views.paciente_detail, name='paciente_detail'),
    path('paciente/<int:pk>/update/', views.paciente_update, name='paciente_update'),
    path('paciente/<int:pk>/delete/', views.paciente_delete, name='paciente_delete'),
]