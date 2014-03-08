from django.db import models


class Reino(models.Model):
    nombre = models.CharField(max_length=400)

    def __unicode__(self):
        return self.nombre


class SubReino(models.Model):
    nombre = models.CharField(max_length=400)
    reino = models.ForeignKey(Reino)

    def __unicode__(self):
        return self.nombre


class Division(models.Model):
    nombre = models.CharField(max_length=400)
    subreino = models.ForeignKey(SubReino)

    def __unicode__(self):
        return self.nombre


class SubDivision(models.Model):
    nombre = models.CharField(max_length=400)
    division = models.ForeignKey(Division)

    def __unicode__(self):
        return self.nombre


class Clase(models.Model):
    nombre = models.CharField(max_length=400)
    subdivision = models.ForeignKey(SubDivision)

    def __unicode__(self):
        return self.nombre


class Orden(models.Model):
    nombre = models.CharField(max_length=400)
    clase = models.ForeignKey(Clase)

    def __unicode__(self):
        return self.nombre


class Familia(models.Model):
    nombre = models.CharField(max_length=400)
    orden = models.ForeignKey(Clase)

    def __unicode__(self):
        return self.nombre