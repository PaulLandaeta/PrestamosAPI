from django.db import models
from .validators import validar_par
from .validators import validation_tipo_credito
from .validators import monto
from .validators import edad


from django.core.validators import EmailValidator


class TipoDeCredito(models.Model):
    nombre = models.CharField(
        max_length=100,
        validators=[
            validation_tipo_credito,
        ],
    )

    def __str__(self):
        return self.nombre


class Asesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        validators=[
            edad,
        ],
    )

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.edad}"


class Credito(models.Model):
    id_credito = models.AutoField(primary_key=True)
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            monto,
        ],
    )
    fecha_desembolso = models.DateField()
    numero_cuotas = models.PositiveIntegerField(
        validators=[
            validar_par,
        ]
    )
    id_tipo = models.ForeignKey(TipoDeCredito, on_delete=models.CASCADE)
    frecuencia_de_pago = models.CharField(max_length=100)
    id_asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    ciclo = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id_asesor} - {self.id_tipo} - {self.total}"


class Cuota(models.Model):
    id_cuota = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=100, decimal_places=2)
    fecha = models.DateField()
    id_tipo = models.ForeignKey(TipoDeCredito, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_cuota} - {self.fecha} - {self.total}"
