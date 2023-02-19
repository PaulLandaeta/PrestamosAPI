from django.shortcuts import render

from rest_framework import viewsets
from .models import Asesor
from .serializers import AsesorSerializer


# Create your views here.

class AsesorViewSet(viewsets.ModelViewSet):
    queryset = Asesor.objects.all()
    serializer_class = AsesorSerializer
    
class AsesorList(viewsets.ModelViewSet):
    serializer_class = AsesorSerializer
    queryset = Asesor.objects.all()

class AsesorDetail(viewsets.ModelViewSet):
    serializer_class = AsesorSerializer
    queryset = Asesor.objects.all()

class AsesorCreate(viewsets.ModelViewSet):
    serializer_class = AsesorSerializer
    queryset = Asesor.objects.all()