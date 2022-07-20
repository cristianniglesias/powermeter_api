
from django.urls import path

from . import views

app_name = 'medir_app'

urlpatterns = [
    path('save/', views.MedicionesViewSet.as_view(), name='mediciones_list'),
    path('get/max/', views.MedicionesViewSet.number_max, name='number_max'),
    path('get/min/', views.MedicionesViewSet.number_min, name='number_min'),
    path('get/avg/', views.MedicionesViewSet.number_promedio, name='number_promedio'),
]
