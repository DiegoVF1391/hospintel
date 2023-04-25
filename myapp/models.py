from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    domicio = models.CharField(max_length=200)
    sexo = models.CharField(max_length=200)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

class Cita(models.Model):
    fecha_cita = models.DateField()
    padecimiento = models.CharField(max_length=200)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)