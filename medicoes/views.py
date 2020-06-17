from django.shortcuts import render
from rest_framework import generics
from .models import Parametros
from .serializers import ParametrosSerializer

# Create your views here.
class ParametrosList(generics.ListCreateAPIView):

    queryset = Parametros.objects.all()
    serializer_class = ParametrosSerializer

