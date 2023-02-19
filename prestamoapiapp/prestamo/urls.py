from django.urls import path
from . import views

urlpatterns = [
    path("tipoDeCreditos", views.TipoDeCreditos, name="TipoDeCreditos"),
    path("asesor", views.AsesorCreate, name="asesores"),
    path("creditos", views.creditoFormView, name="creditos"),
    path("", views.index, name="index"),
]
