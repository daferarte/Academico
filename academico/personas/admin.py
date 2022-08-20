from django.contrib import admin
from .models import personas, tipoDocumento

# Register your models here.

class tipoDocumentoAdmin(admin.ModelAdmin):
    readonly_fields = ('nombre',)
    search_fields = ('nombre',)
    list_display = ('nombre','descripcion',)
    ordering=('-nombre',)

class personasAdmin(admin.ModelAdmin):
    readonly_fields = ('cedula',)
    search_fields = ('cedula','fNacimiento',)
    list_display = ('cedula','fNacimiento',)
    ordering=('-create_at',)

admin.site.register(tipoDocumento, tipoDocumentoAdmin)
admin.site.register(personas, personasAdmin)