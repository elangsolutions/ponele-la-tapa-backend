from django.db import models
from colorfield.fields import ColorField


class Texto(models.Model):
    codigo = models.CharField(
        max_length=10, blank=False, null=False, unique=True)
    texto = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.texto


class Color(models.Model):
    codigo = models.CharField(
        max_length=3, blank=False, null=False, unique=True)
    color = ColorField(default='#FFFFFF', blank=False, null=False)

    def __str__(self):
        return '{codigo}'.format(codigo=self.codigo)


class Caracteristica(models.Model):
    caracteristica = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.caracteristica


class Tapa(models.Model):
    linea = models.CharField(max_length=20, blank=False,
                             null=False, default="Clasica")
    modelo = models.CharField(max_length=100, blank=False, null=False)
    ancho = models.FloatField(blank=False, null=False, default=30)
    alto = models.FloatField(blank=False, null=False, default=30)
    caracteristica = models.ManyToManyField(
        Caracteristica, related_name="caracteristica_tapa")
    comprar = models.BooleanField(default=False)

    def __str__(self):
        return self.modelo


class TapaImage(models.Model):
    imagen = models.ImageField(
        upload_to='tapa-image-files/', blank=False, null=False)
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, related_name="color_imagen",
        blank=False, null=False)
    tapa = models.ForeignKey(
        Tapa, on_delete=models.CASCADE, related_name="tapa_imagen",
        blank=False, null=False)

    def __str__(self):
        return self.imagen.name


class Loza(models.Model):
    linea = models.CharField(max_length=20, blank=False,
                             null=False, default="Loza")
    imagen = models.ImageField(
        upload_to='tapa-files/', blank=True, null=True)
    # cambiar a false false
    moderna = models.ForeignKey(
        Tapa, on_delete=models.CASCADE, related_name="tapa_moderna",
        blank=True, null=True)
    clasica = models.ForeignKey(
        Tapa, on_delete=models.CASCADE, related_name="tapa_clasica",
        blank=True, null=True)
    madera_metalico = models.ForeignKey(
        Tapa, on_delete=models.CASCADE, related_name="tapa_madera_metalico",
        blank=True, null=True)
    madera_plastico = models.ForeignKey(
        Tapa, on_delete=models.CASCADE, related_name="tapa_madera_plastico",
        blank=True, null=True)

    def __str__(self):
        return self.linea
