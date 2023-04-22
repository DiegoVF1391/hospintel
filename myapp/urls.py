from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_image, name='upload'),
]