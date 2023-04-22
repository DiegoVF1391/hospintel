from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm
import pytesseract
from PIL import Image
import os

def dashboard(request):
    return render(request, 'dashboard.html')

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
            text = pytesseract.image_to_string(img)
            # Eliminar la imagen temporal
            f.close()
            os.remove('temp_image.jpg')
            # Mostrar el texto extraído en la consola
            print(text)
            # Redirigir a la página de dashboard
            return redirect('dashboard')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def redirect_to_dashboard(request):
    return redirect('dashboard')