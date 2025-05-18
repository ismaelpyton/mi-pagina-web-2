from django.db import models
from django.utils import timezone

class Reserva(models.Model):
    SERVICIOS_CHOICES = [
        ('simultanea', 'Interpretación Simultánea'),
        ('consecutiva', 'Interpretación Consecutiva'),
        ('especializados', 'Servicios Especializados'),
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]

    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    servicio = models.CharField(max_length=20, choices=SERVICIOS_CHOICES)
    fecha_evento = models.DateField()
    horas_servicio = models.IntegerField()
    metodo_pago = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_payment_id = models.CharField(max_length=100, blank=True, null=True)
    descripcion_proyecto = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.servicio} - {self.fecha_evento}"

    def calcular_monto(self):
        precios = {
            'simultanea': 150,
            'consecutiva': 120,
            'especializados': 100  # Precio base para evaluación
        }
        
        if self.servicio in ['simultanea', 'consecutiva']:
            # Aplicar descuento por horas
            precio_base = precios[self.servicio]
            if self.horas_servicio > 4:
                precio_base = precio_base * 0.9  # 10% de descuento
            return precio_base * self.horas_servicio
        else:
            return precios['especializados']  # Precio base para evaluación
