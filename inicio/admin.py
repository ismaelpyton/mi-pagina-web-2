from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'servicio', 'fecha_evento', 'estado', 'monto_total', 'fecha_creacion')
    list_filter = ('estado', 'servicio', 'fecha_evento', 'fecha_creacion')
    search_fields = ('nombre', 'email', 'descripcion_proyecto')
    list_editable = ('estado',) # Permite editar el estado directamente desde la lista
    readonly_fields = ('fecha_creacion', 'monto_total') # Campos que no se deben editar manualmente aquí

    fieldsets = (
        (None, {
            'fields': ('nombre', 'email', 'servicio', 'metodo_pago')
        }),
        ('Detalles del Evento', {
            'fields': ('fecha_evento', 'horas_servicio', 'descripcion_proyecto')
        }),
        ('Estado y Pago', {
            'fields': ('estado', 'monto_total', 'stripe_payment_id', 'fecha_creacion')
        }),
    )

    def get_queryset(self, request):
        # Ordenar por fecha de creación descendente por defecto
        return super().get_queryset(request).order_by('-fecha_creacion')

# Si tienes otros modelos que quieras registrar, puedes hacerlo aquí.
# Por ejemplo:
# from .models import OtroModelo
# admin.site.register(OtroModelo)
