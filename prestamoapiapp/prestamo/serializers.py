from rest_framework import serializers
from .models import Asesor
from .models import TipoDeCredito
class AsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asesor
        fields = '__all__'

class TipoDeCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeCredito
        fields = '__all__'