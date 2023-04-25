from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ImageForm
import pytesseract
import re
import os
from datetime import datetime
from myapp.models import Cita
from .forms import ImageForm, PacienteForm
from PIL import Image
from .models import Paciente

#vista para el dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

#vista para subida de la imagen
def upload_image(request):
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            # Guardar la imagen temporalmente
            with open('temp_image.jpg', 'wb+') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            # Procesar la imagen utilizando pytesseract
            img = Image.open('temp_image.jpg')
            text = pytesseract.image_to_string(img, lang='spa')
            # Eliminar la imagen temporal
            f.close()
            os.remove('temp_image.jpg')
            # Mostrar el texto extraído en la consola
            text = text.replace("º", "o")
            print(text)

            # Procesar el texto para extraer la información relevante
            fecha_match = re.search(r'Fecha: (\d{2}/\d{2}/\d{4})', text)
            padecimiento_match = re.search(r'Padecimiento: (.+)', text)

            print(fecha_match, padecimiento_match)
            if fecha_match and padecimiento_match:
            
                # Crear una instancia del modelo Receta
                fecha_cita = datetime.strptime(fecha_match.group(1), '%d/%m/%Y')
                padecimiento_cita = padecimiento_match.group(1)
                print(fecha_cita, padecimiento_cita)
                cita = Cita(fecha_cita=fecha_cita, padecimiento=padecimiento_cita, paciente_id=1)
                #print(cita)
                ## Guardar la instancia en la base de datos
                cita.save()
                
            # Redirigir a la página de dashboard
            return redirect('dashboard')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def redirect_to_dashboard(request):
    return redirect('dashboard')

#FUNCIONES PARA PACIENTES
def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente_list.html', {'pacientes': pacientes})

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'paciente_form.html', {'form': form})

def paciente_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'paciente_detail.html', {'paciente': paciente})

def paciente_update(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save(commit=False)
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'paciente_form.html', {'form': form})

def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('paciente_list')