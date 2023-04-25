from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=60, default="No ingresado")
    apellido_materno = models.CharField(max_length=60, default="No ingresado")
    domicilio = models.CharField(max_length=200)
    sexo = models.CharField(max_length=200)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20)

class Cita(models.Model):
    fecha_cita = models.DateField()
    padecimiento = models.CharField(max_length=200)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)