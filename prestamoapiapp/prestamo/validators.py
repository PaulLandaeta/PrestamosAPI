from django.core.exceptions import ValidationError


def validar_par(value):
    if value % 2 != 0:
        raise ValidationError("%(value)s no es un numero par", params={"value": value})


def validation_tipo_credito(value):
    if value == "no permitido":
        raise ValidationError("No permitido")


def monto(value):
    if value > 5000:
        raise ValidationError("monto no permitido tiene que ser menor que 5000")


def edad(value):
    if value < 18:
        raise ValidationError("edad no permitido tiene que tener mayor de 18 años")
