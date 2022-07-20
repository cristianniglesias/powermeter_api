from django.db import models
from model_utils.models import TimeStampedModel

class Mediciones(TimeStampedModel):
    valor_medido = models.FloatField('valor medido', null=False, blank=True)

    def __str__(self):
        return str(self.valor_medido)
