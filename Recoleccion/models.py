from django.db import models


class Recolector(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=400)
    email = models.EmailField(blank=True)
    telefono = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.nombre + " " + self.apellidos


class Lugar:
    ISLA_CHOICE = (
        (0, 'Gran Canaria'),
        (1, 'Tenerife'),
        (2, 'La Palma'),
        (3, 'La Gomera'),
        (4, 'El Hierro'),
        (5, 'Lanzarote'),
        (6, 'Fuerteventura'),
    )

    isla = models.IntegerField(choices=ISLA_CHOICE)
    #municipio = models.IntegerField(choices=MUNICIPIO_CHOICES)