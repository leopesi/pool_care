from django.contrib import admin
from .models import Parametros

@admin.register(Parametros)
class Parametrosadmin(admin.ModelAdmin):
    list_display = ('alcalinidade', 'ph', 'cloro', 'agua', 'trat_cloro')

