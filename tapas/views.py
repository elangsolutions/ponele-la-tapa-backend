from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Tapa, TapaImage, Loza, Texto
from .serializers import TapasSerializer, TapaSerializer, LozasSerializer, TextosSerializer


class TapasViewSet(generics.ListAPIView):
    queryset = Tapa.objects.all()
    serializer_class = TapasSerializer
    permission_classes = [AllowAny]


class TapaViewSet(generics.RetrieveAPIView):
    queryset = Tapa.objects.all()
    serializer_class = TapaSerializer
    permission_classes = [AllowAny]


class LozasViewSet(generics.ListAPIView):
    queryset = Loza.objects.all()
    serializer_class = LozasSerializer
    permission_classes = [AllowAny]


class TextosViewSet(generics.ListAPIView):
    queryset = Texto.objects.all()
    serializer_class = TextosSerializer
    permission_classes = [AllowAny]
