from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/simultanea/', views.servicio_simultanea, name='servicio_simultanea'),
    path('servicios/consecutiva/', views.servicio_consecutiva, name='servicio_consecutiva'),
    path('servicios/especializados/', views.servicio_especializados, name='servicio_especializados'),
    path('procesar-pago/', views.procesar_pago, name='procesar_pago'),
    path('sobre-mi/', views.vista_sobre_mi, name='sobre_mi'),
    path('contacto/', views.vista_contacto, name='contacto'),
    path('productos/', views.vista_productos, name='productos'),
    path('prueba/', views.vista_prueba, name='prueba'),
    path('clientes/aivepet/', views.aivepet_detalle_vista, name='aivepet_detalle'),
    path('clientes/universidad-internacional-abc/', views.universidad_detalle_vista, name='universidad_detalle'),
    path('clientes/corporacion-global-def/', views.corporacion_detalle_vista, name='corporacion_detalle'),
    path('clientes/hayco/', views.hayco_detalle_vista, name='hayco_detalle'),
    path('solicitud-confirmada/<int:reserva_id>/', views.confirmacion_solicitud_vista, name='confirmacion_solicitud'),
]
