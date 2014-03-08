from django.shortcuts import render
from django.http import HttpResponse
from models import Pie, Sombrero


def init(request):
    try:
        Pie.objects.get(pie=0)
        html = "<html><body>Inicializacion ya hecha anteriormente</body></html>"
        return HttpResponse(html)
    except:
        for x in Pie.PIE_CHOICES:
            pie = Pie(pie=x[0])
            pie.save()

        for x in Sombrero.SOMBRERO_CHOICES:
            sombrero = Sombrero(sombrero=x[0])
            sombrero.save()
        html = "<html><body>Inicializacion Correcta</body></html>"
        return HttpResponse(html)