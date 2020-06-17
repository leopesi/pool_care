from rest_framework import serializers
from .models import Parametros

class ParametrosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Parametros
        fields = ('id', 'alcalinidade', 'ph', 'cloro', 'agua', 'trat_alcalinidade', 'trat_ph', 'trat_cloro')