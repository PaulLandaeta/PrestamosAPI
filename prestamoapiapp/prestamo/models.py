from django.db import models

class TipoDeCredito(models.Model):
    nombre = models.CharField(max_length=100)

class Asesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

class Credito(models.Model):
    id_credito = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_desembolso = models.DateField()
    numero_cuotas = models.PositiveIntegerField()
    id_tipo = models.ForeignKey(TipoDeCredito, on_delete=models.CASCADE)
    frecuencia_de_pago = models.CharField(max_length=100)
    id_asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    ciclo = models.PositiveIntegerField()
    