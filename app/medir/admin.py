from django.contrib import admin
from app.medir.models import (Mediciones)
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Mediciones)
class MedicionesAdmin(SimpleHistoryAdmin):
    list_display = ['valor_medido']
