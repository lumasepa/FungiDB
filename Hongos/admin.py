from django.contrib import admin
from models import *


class HongoAdmin(admin.ModelAdmin):
    search_fields = ['especie', 'nombre_comun']
    list_display = ('especie', 'nombre_comun')


class HimenioColorAdmin(admin.ModelAdmin):
    search_fields = ['color',]
    list_display = ('color',)


class BiotopoAdmin(admin.ModelAdmin):
    search_fields = ['nombre',]
    list_display = ('nombre',)


admin.site.register(Hongo, HongoAdmin)
admin.site.register(HimenioColor, HimenioColorAdmin)
admin.site.register(Biotopo, BiotopoAdmin)



