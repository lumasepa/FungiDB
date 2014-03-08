from django.db import models
from Biota.models import Familia


class Pie(models.Model):
    PIE_CHOICES = (
        (0, 'AUSENTE'),
        (1, 'DELGADO'),
        (2, 'GRUESO'),
        (3, 'HUECO'),
        (4, 'MACIZO'),
        (5, 'SINUOSO'),
        (6, 'CON_ANILLO_SIMPLE'),
        (7, 'CON_ANILLO_DOBLE'),
        (8, 'CON_VOLVA'),
        (9, 'RADICANTE'),
        (10, 'BULBOSO'),
        (11, 'CLAVIFORME'),
        (12, 'EXENTRICO'),
        (13, 'LATERAL'),
        (14, 'FIBROSO'),
        (15, 'ROMPE_COMO_TIZA'),
        (16, 'OTRO'),
    )
    pie = models.IntegerField(choices=PIE_CHOICES)

    def __unicode__(self):
        return self.PIE_CHOICES[self.pie][1]


class Sombrero(models.Model):
    SOMBRERO_CHOICES = (
        (0, 'NO_PROCEDE'),
        (1, 'HEMISFERICO'),
        (2, 'CONVEXO'),
        (3, 'APLANADO'),
        (4, 'ACAMPANADO'),
        (5, 'MAMELONADO'),
        (6, 'CONICO'),
        (7, 'OVOIDE'),
        (8, 'DEPRIMIDO'),
        (9, 'UMBILICADO'),
        (10, 'EMBUDADO_INFUNDIBULIFORME'),
        (11, 'OTRO'),
    )
    sombrero = models.IntegerField(choices=SOMBRERO_CHOICES)

    def __unicode__(self):
        return self.SOMBRERO_CHOICES[self.sombrero][1]


class HimenioColor(models.Model):
    color = models.CharField(max_length=200)

    def __unicode__(self):
        return self.color


class Biotopo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre


def image_file_name(instance, filename):
    return 'hongosimages/'.join([str(instance.especie), "_", filename])


class Hongo(models.Model):
    CARPOFORO_CHOICES = (
        (0, 'LAMINAS'),
        (1, 'POROS'),
        (2, 'AGUIJONES'),
        (3, 'LABERINTOS'),
        (4, 'FALSAS_LAMINAS_CANTHARELLA'),
        (5, 'CONCAVO_PEZIZA'),
        (6, 'ESFERICO_GASTOMICETES'),
        (7, 'BOMBILLA_LYCOPERDON'),
        (8, 'CORAL_RAMARIA'),
        (9, 'ESTRELLA_GEASTRUM'),
        (10, 'CONCHA_CON_PIE_PLEROTUS'),
        (11, 'COLMENILLA'),
        (12, 'POLIPORO'),
        (13, 'CAMBIANTE_AFILOFORALES'),
        (14, 'OTRO'),
    )
    HIMENIO_CHOICES = (
        (0, 'LAMINAS'),
        (1, 'PLIEGUES'),
        (2, 'LISO'),
        (3, 'POROS'),
        (4, 'AGUIJONES'),
        (5, 'LABERINTO'),
        (6, 'MASIVO'),
        (7, 'GELATINOSO'),
        (8, 'CAMBIANTE_AFILOFORALES'),
        (9, 'OTRO'),
    )
    HIMENIO_UNION_PIE_CHOICES = (
        (0, 'NO_PROCEDE'),
        (1, 'LIBRES'),
        (2, 'ESCOTADAS'),
        (3, 'ADNATAS'),
        (4, 'RECURRENTES'),
        (5, 'OTRO'),
    )
    COMESTIBILIDAD_CHOICES = (
        (0, 'EXELENTE_COMESTIBLE'),
        (1, 'COMESTIBLE'),
        (2, 'SIN_VALOR_CULINARIO'),
        (3, 'NO_COMESTIBLE'),
        (4, 'TOXICO'),
        (5, 'TOXICO_MORTAL'),
        (6, 'TOXICO_CON_ALCOHOL'),
    )
    PIE_CHOICES = (
        (0, 'AUSENTE'),
        (1, 'DELGADO'),
        (2, 'GRUESO'),
        (3, 'HUECO'),
        (4, 'MACIZO'),
        (5, 'SINUOSO'),
        (6, 'CON_ANILLO_SIMPLE'),
        (7, 'CON_ANILLO_DOBLE'),
        (8, 'CON_VOLVA'),
        (9, 'RADICANTE'),
        (10, 'BULBOSO'),
        (11, 'CLAVIFORME'),
        (12, 'EXENTRICO'),
        (13, 'LATERAL'),
        (14, 'FIBROSO'),
        (15, 'ROMPE_COMO_TIZA'),
        (16, 'OTRO'),
    )
    especie = models.CharField(max_length=400)
    nombre_comun = models.CharField(max_length=400)
    familia = models.ForeignKey(Familia)
    carpoforo = models.IntegerField(choices=CARPOFORO_CHOICES)
    carpoforo_txt = models.TextField()
    himenio = models.IntegerField(choices=HIMENIO_CHOICES)
    himenio_color = models.ManyToManyField(HimenioColor)
    himenio_union_pie = models.IntegerField(choices=HIMENIO_UNION_PIE_CHOICES)
    himenio_txt = models.TextField()
    sombrero = models.ManyToManyField(Sombrero)
    sombrero_txt = models.TextField()
    pie = models.ManyToManyField(Pie)
    pie_txt = models.TextField()
    gleba = models.BooleanField(default=False)
    subgleba = models.BooleanField(default=False)
    peridio = models.BooleanField(default=False)
    exoperidio = models.BooleanField(default=False)
    gasteromicete_txt = models.TextField()
    comestibilidad = models.IntegerField(choices=COMESTIBILIDAD_CHOICES)
    comestibilidad_txt = models.TextField()
    olor_txt = models.TextField()
    biotopo = models.ManyToManyField(Biotopo)
    confusiones_particularidades = models.TextField()
    esporada_txt = models.TextField()
    esporas_txt = models.TextField()
    foto_macroscopica_1 = models.ImageField(upload_to=image_file_name)
    foto_macroscopica_2 = models.ImageField(upload_to=image_file_name)
    foto_macroscopica_3 = models.ImageField(upload_to=image_file_name)
    foto_macroscopica_4 = models.ImageField(upload_to=image_file_name)
    foto_microscopica_1 = models.ImageField(upload_to=image_file_name)
    foto_microscopica_2 = models.ImageField(upload_to=image_file_name)
    foto_microscopica_3 = models.ImageField(upload_to=image_file_name)

    def __unicode__(self):
        return self.especie

