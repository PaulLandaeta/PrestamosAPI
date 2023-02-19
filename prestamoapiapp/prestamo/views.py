from django.shortcuts import render
from rest_framework import viewsets
from .models import Asesor
from .serializers import AsesorSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TipoDeCredito
from .serializers import TipoDeCreditoSerializer

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


class TipoDeCreditoAPI(APIView):
    def get(self, request):
        tipos = TipoDeCredito.objects.all()
        serializer = TipoDeCreditoSerializer(tipos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TipoDeCreditoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)