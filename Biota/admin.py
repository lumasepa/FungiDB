from django.contrib import admin
from models import *


class ReinoAdmin(admin.ModelAdmin):
    search_fields = ['nombre',]
    list_display = ('nombre',)


class SubReinoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'reino']
    list_display = ('nombre', 'reino')


class DivisionAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'subreino']
    list_display = ('nombre', 'subreino')


class SubDivisionAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'division']
    list_display = ('nombre', 'division')


class ClaseAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'subdivision']
    list_display = ('nombre', 'subdivision')


class OrdenAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'clase']
    list_display = ('nombre', 'clase')


class FamiliaAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'orden']
    list_display = ('nombre', 'orden')


admin.site.register(Reino, ReinoAdmin)
admin.site.register(SubReino, SubReinoAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(SubDivision, SubDivisionAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(Familia, FamiliaAdmin)