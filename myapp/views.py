from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm
import pytesseract
from PIL import Image
import os
import numpy as np
import cv2

def dashboard(request):
    return render(request, 'dashboard.html')

def upload_image(request):
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            # Leer la imagen en formato numpy array utilizando OpenCV
            img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            # Convertir la imagen a escala de grises
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Aplicar binarización adaptativa para mejorar el contraste de la imagen
            gray = cv2.medianBlur(gray, 3)
            cv2.imshow('Image',gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # Extraer el texto utilizando pytesseract
            text = pytesseract.image_to_string(gray, lang='spa')
            # Mostrar el texto extraído en la consola
            text = text.replace("º", "o")
            print(text)
            # Redirigir a la página de dashboard
            return redirect('dashboard')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def redirect_to_dashboard(request):
    return redirect('dashboard')