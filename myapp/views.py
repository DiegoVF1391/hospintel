from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm

def dashboard(request):
    return render(request, 'dashboard.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Procesar la imagen aquí
            form.save()
            return redirect('dashboard')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def redirect_to_dashboard(request):
    return redirect('dashboard')