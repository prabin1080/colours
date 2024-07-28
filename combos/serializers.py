from rest_framework.serializers import ModelSerializer

from .models import (
    Project, Colour, Paint, ComboEffect
)


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ColourSerializer(ModelSerializer):
    class Meta:
        model = Colour
        fields = '__all__'


class PaintSerializer(ModelSerializer):
    class Meta:
        model = Paint
        fields = '__all__'


class ComboEffectSerializer(ModelSerializer):
    class Meta:
        model = ComboEffect
        fields = '__all__'
