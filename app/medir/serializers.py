from app.medir.models import Mediciones
from rest_framework import serializers


class MedicionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mediciones
        fields = ['valor_medido']

    def is_valid(self, raise_exception=False):
        return super().is_valid(raise_exception)

