
from django.http import Http404
from app.medir.models import Mediciones
from django.db.models import Max, Avg, Min
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MedicionesSerializer

class MedicionesViewSet(APIView):
    queryset = Mediciones.objects.all()
    serializer_class = MedicionesSerializer

    def get(self, request, format=None, *args, **kwargs):
        medicion = Mediciones.objects.all()
        serializer = MedicionesSerializer(medicion, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data_all = request.data.get('sensor_data')
        if data_all:
            for data_one in data_all:
                serializer = MedicionesSerializer(
                    data={'valor_medido': data_one})
                if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
            info = {'Success': True}
            return Response(info, status=status.HTTP_201_CREATED)
        info = {'Error': 'Tipo de entrada no valida'}
        return Response(info, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def number_max(request):
        number_max = Mediciones.objects.all().aggregate(Max('valor_medido'))
        if number_max['valor_medido__max']:
            serializer = {'max': number_max['valor_medido__max']}
            return Response(serializer, status=status.HTTP_200_OK)
        info = {'Información': 'Aun no hay metricas para calcular el maximo'}
        return Response(info, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def number_promedio(request):
        number_avg = Mediciones.objects.all().aggregate(Avg('valor_medido'))
        if  number_avg['valor_medido__avg']:
            serializer = {'avg': number_avg['valor_medido__avg']}
            return Response(serializer, status=status.HTTP_200_OK)
        info = {'Información': 'Aun no hay metricas para calcular el promedio'}
        return Response(info, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def number_min(request):
        number_min = Mediciones.objects.all().aggregate(Min('valor_medido'))
        if number_min['valor_medido__min']:
            serializer = {'min': number_min['valor_medido__min']}
            return Response(serializer, status=status.HTTP_200_OK)
        info = {'Información': 'Aun no hay metricas para calcular el minimo'}
        return Response(info, status=status.HTTP_200_OK)
        
        
        
