from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Reserva
from datetime import datetime
import json

def inicio(request):
    return render(request, 'inicio/inicio.html')

def servicio_simultanea(request):
    return render(request, 'inicio/servicio_simultanea.html')

def servicio_consecutiva(request):
    return render(request, 'inicio/servicio_consecutiva.html')

def servicio_especializados(request):
    return render(request, 'inicio/servicio_especializados.html')

@csrf_exempt
def procesar_pago(request):
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            servicio = request.POST.get('servicio')
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            fecha_evento = request.POST.get('fecha_evento')
            horas_servicio = int(request.POST.get('horas_servicio', 1))
            metodo_pago = request.POST.get('metodo_pago')
            descripcion = request.POST.get('descripcion_proyecto', '')

            # Crear la reserva
            reserva = Reserva(
                nombre=nombre,
                email=email,
                servicio=servicio,
                fecha_evento=datetime.strptime(fecha_evento, '%Y-%m-%d').date(),
                horas_servicio=horas_servicio,
                metodo_pago=metodo_pago,
                descripcion_proyecto=descripcion
            )
            
            # Calcular el monto total
            monto_total = reserva.calcular_monto()
            reserva.monto_total = monto_total
            reserva.save()

            # Redirigir a la página de confirmación en lugar de mostrar mensaje flash aquí
            return HttpResponseRedirect(reverse('confirmacion_solicitud', args=[reserva.id]))

        except Exception as e:
            messages.error(request, f'Error al procesar la reserva: {str(e)}')
            return HttpResponseRedirect(reverse('inicio'))

    return HttpResponseRedirect(reverse('inicio'))

def vista_inicio(request):
    # Datos ficticios de clientes para demostración (repetidos aquí para pasarlos a la plantilla de inicio)
    datos_clientes = {
        'aivepet': { # Cambiada la clave del diccionario
            'nombre': 'AIVEPET',
            'descripcion_corta': 'Interpretación simultánea Chino-Español para conferencia internacional.',
            'secciones': [ # Adaptado a la nueva estructura
                {
                    'descripcion': 'Colaboré con Empresa Tecnológica XYZ durante su conferencia anual internacional, proporcionando interpretación simultánea Chino-Español para todas las ponencias magistrales y sesiones de preguntas y respuestas. Esto facilitó una comunicación fluida y efectiva entre los ponentes chinos y la audiencia de habla hispana, contribuyendo al éxito del evento.',
                    'imagen': {'url': 'imagenes/cliente1.jpg', 'descripcion': 'Imagen principal del evento XYZ.'}
                }
            ],
            'servicios_prestados': ['Interpretación Simultánea', 'Soporte Técnico para Equipos de Interpretación'],
            'testimonio': 'La profesionalidad y precisión de Edilian fueron clave para nuestro evento. ¡Altamente recomendada!',
            'descripcion_larga_en': ''
        },
        'universidad-internacional-abc': {
            'nombre': 'Universidad Internacional ABC',
            'descripcion_corta': 'Interpretación consecutiva para seminarios de investigación con académicos chinos.',
             'secciones': [ # Adaptado a la nueva estructura
                {
                    'descripcion': 'Para la Universidad Internacional ABC, ofrecí servicios de interpretación consecutiva durante una serie de seminarios de investigación con académicos visitantes de China. También facilité mesas redondas bilingües, asegurando que todos los participantes pudieran comprender y contribuir plenamente a las discusiones.',
                    'imagen': {'url': 'imagenes/cliente2.jpg', 'descripcion': 'Seminario con académicos visitantes.'}
                }
            ],
            'servicios_prestados': ['Interpretación Consecutiva', 'Traducción de Material Académico'],
            'testimonio': 'Un servicio impecable que enriqueció nuestros intercambios académicos.',
            'descripcion_larga_en': ''
        },
        'corporacion-global-def': {
            'nombre': 'Corporación Global DEF',
            'descripcion_corta': 'Interpretación en negociaciones comerciales con socios estratégicos en Asia.',
             'secciones': [ # Adaptado a la nueva estructura
                {
                    'descripcion': 'Asistí a Corporación Global DEF en negociaciones comerciales cruciales con socios estratégicos en Asia. Mi rol fue proveer interpretación consecutiva Español-Inglés-Chino, garantizando la exactitud en la comunicación de términos contractuales y estrategias de negocio. También traduje documentos legales y presentaciones corporativas.',
                    'imagen': {'url': 'imagenes/cliente3.jpg', 'descripcion': 'Reunión de negociación con DEF Corp.'}
                }
            ],
            'servicios_prestados': ['Interpretación Consecutiva en Negociaciones', 'Traducción de Documentos Legales'],
            'testimonio': 'Su habilidad para manejar la terminología técnica y la presión de las negociaciones fue excepcional.',
            'descripcion_larga_en': "I strategically contributed to the success of Corporación Global DEF in crucial business negotiations with its main partners in Asia. Through expert Spanish-English-Chinese consecutive interpretation services, I ensured fidelity and accuracy in the communication of contractual clauses and business plans, key elements for decision-making and the advancement of negotiations. My role also included the accurate translation of sensitive legal documentation and high-level corporate presentations."
        },
        'hayco': {
            'nombre': 'HAYCO',
            'descripcion_corta': 'Soporte lingüístico para equipo técnico internacional.',
            'secciones': [ # Nueva estructura para múltiples secciones
                {
                    'descripcion': 'I led the smooth integration of an eight-member technical team into the work environment of a mold project for a key HAYCO client. I utilized my extensive technical knowledge and fluency in English and Mandarin to oversee the proper maintenance and assembly of the mold, ensuring all operations and communications were conducted efficiently in English.',
                    'imagen': {'url': 'imagenes/placeholder_hayco.jpg', 'descripcion': 'Imagen del proyecto HAYCO - Sección 1'}
                },
                {
                    'descripcion': 'Aquí iría la segunda descripción para la segunda imagen de HAYCO.', # Segunda descripción
                    'imagen': {'url': 'imagenes/placeholder_detalle1.jpg', 'descripcion': 'Imagen del proyecto HAYCO - Sección 2'} # Segunda imagen
                }
            ],
            'servicios_prestados': ['Interpretación Técnica', 'Soporte Lingüístico en Planta'],
            'testimonio': 'La asistencia de Edilian fue fundamental para la integración del equipo técnico.',
            'descripcion_larga_en': ''
        }
    }
    return render(request, 'inicio/inicio.html', {'nombre': 'Ismael', 'clientes': datos_clientes.items()})

def vista_sobre_mi(request):
    return render(request, 'inicio/sobre_mi.html', {'nombre': 'Ismael'})

def vista_contacto(request):
    return render(request, 'inicio/contacto.html', {
        'correo': 'ismaelbatista2021@gmail.com',
        'numero_de_telefono': '829-934-0964'
    })

def vista_productos(request):
    return render(request, 'inicio/productos.html')

def vista_prueba(request):
    return render(request,'inicio/index.html')

def aivepet_detalle_vista(request):
    return render(request, 'inicio/aivepet_detalle.html')

def universidad_detalle_vista(request):
    return render(request, 'inicio/universidad_detalle.html')

def corporacion_detalle_vista(request):
    return render(request, 'inicio/corporacion_detalle.html')

def hayco_detalle_vista(request):
    return render(request, 'inicio/hayco_detalle.html')

def confirmacion_solicitud_vista(request, reserva_id):
    try:
        reserva = Reserva.objects.get(pk=reserva_id)
    except Reserva.DoesNotExist:
        # Manejar el caso de que la reserva no exista, quizás redirigir a inicio con un error
        messages.error(request, "La solicitud de reserva no fue encontrada.")
        return HttpResponseRedirect(reverse('inicio'))
    
    context = {
        'reserva': reserva
    }
    return render(request, 'inicio/confirmacion_solicitud.html', context)
