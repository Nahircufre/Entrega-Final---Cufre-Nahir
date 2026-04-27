from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# 📄 MODELO PRINCIPAL (BLOG)
class Page(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='pages/', null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# 💬 MODELO MENSAJERÍA
class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_enviados")
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_recibidos")
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.remitente} → {self.destinatario}"