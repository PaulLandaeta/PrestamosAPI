from django.shortcuts import render
from rest_framework import viewsets
from .models import Asesor
from .serializers import AsesorSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TipoDeCredito
from .serializers import TipoDeCreditoSerializer
from django.http import HttpResponse

from .models import TipoDeCredito
from .models import Credito
from .forms import CreditoForm
from django.shortcuts import get_object_or_404


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


def index(request):
    return HttpResponse("Hola Mundo")


def TipoDeCreditos(request):
    post_nombre = request.POST.get("nombre")
    if post_nombre:
        q = TipoDeCredito(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        TipoDeCreditos = TipoDeCredito.objects.filter(nombre__contains=filtro_nombre)
    else:
        TipoDeCreditos = TipoDeCredito.objects.all()
    return render(request, "form_tipoCredito.html", {"TipoDeCreditos": TipoDeCreditos})


def AsesorCreate(request):
    post_nombre = request.POST.get("nombre")
    post_apellido = request.POST.get("apellido")
    post_edad = request.POST.get("edad")

    if post_nombre:
        q = Asesor(nombre=post_nombre, apellido=post_apellido, edad=post_edad)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        asesor = Asesor.objects.filter(nombre__contains=filtro_nombre)
    else:
        asesor = Asesor.objects.all()
    return render(request, "form_asesor.html", {"asesores": asesor})


def creditoFormView(request):
    form = CreditoForm()
    credito = None
    id_producto = request.GET.get("id")
    if id_producto:
        credito = get_object_or_404(Credito, id=id_producto)

    form = CreditoForm(instance=Credito)
    if request.method == "POST":
        if credito:
            form = CreditoForm(request.POST, instance=credito)
        else:
            form = CreditoForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "form_credito.html", {"form": form})
