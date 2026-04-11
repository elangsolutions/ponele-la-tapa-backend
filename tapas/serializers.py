from rest_framework import serializers

from .models import Tapa, Color, TapaImage, Caracteristica, Loza, Texto


class ColorSerializer(serializers.ModelSerializer):
    """
    Serializer for Color model
    """
    class Meta:
        model = Color
        fields = ('codigo', 'color')


class CaracteristicaSerializer(serializers.ModelSerializer):
    """
    Serializer for Caracteristica model
    """
    class Meta:
        model = Caracteristica
        fields = '__all__'


class TapaImageSerializer(serializers.ModelSerializer):
    """
    Serializer for TapaImage model
    """
    color = ColorSerializer()

    class Meta:
        model = TapaImage
        fields = ('id', 'imagen', 'color')


class TapaSerializer(serializers.ModelSerializer):
    """
    Serializer for Tapa model
    """

    tapa_imagen = TapaImageSerializer(many=True)
    caracteristica = CaracteristicaSerializer(read_only=True, many=True)

    class Meta:
        model = Tapa
        fields = ('id', 'linea', 'modelo', 'ancho',
                  'alto', 'caracteristica', 'tapa_imagen', 'comprar')


class TapasSerializer(serializers.ModelSerializer):
    """
    Serializer for Tapa model
    """

    class Meta:
        model = Tapa
        fields = ('id', 'imagen',)


class LozasSerializer(serializers.ModelSerializer):
    """
    Serializer for Loza model
    """
    class Meta:
        model = Loza
        fields = ('id', 'linea', 'imagen', 'madera_metalico',
                  'madera_plastico', 'moderna', 'clasica')


class TextosSerializer(serializers.ModelSerializer):
    """
    Serializer for Texto model
    """
    class Meta:
        model = Texto
        fields = ('codigo', 'texto')
