from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TipoDeCredito
from .models import Asesor
from .models import Credito


admin.register(Asesor)
admin.register(Credito)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    ordering = ["nombre"]


admin.site.register(TipoDeCredito, AuthorAdmin)
