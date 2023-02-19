"""prestamoapiapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from prestamo.views import AsesorViewSet
from prestamo.views import TipoDeCreditoAPI

router = routers.DefaultRouter()
router.register("asesores", AsesorViewSet)


print(include(router.urls))
urlpatterns = [
    path("admin/", admin.site.urls),
    path("asesores/", include(router.urls)),
    path("tipos/", TipoDeCreditoAPI.as_view(), name="tipos_api"),
    path("prestamo/", include("prestamo.urls")),
]
