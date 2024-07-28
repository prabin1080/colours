from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)

from .models import (
    Project, Colour, Paint, ComboEffect,
)

from .serializers import (
    ProjectSerializer, ColourSerializer, PaintSerializer, ComboEffectSerializer,
)


class ProjectListCreateAPIView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ColourListCreateAPIView(ListCreateAPIView):
    serializer_class = ColourSerializer
    queryset = Colour.objects.all()


class ColourRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ColourSerializer
    queryset = Colour.objects.all()


class PaintListCreateAPIView(ListCreateAPIView):
    serializer_class = PaintSerializer
    queryset = Paint.objects.all()


class PaintRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaintSerializer
    queryset = Paint.objects.all()


class ComboEffectListCreateAPIView(ListCreateAPIView):
    serializer_class = ComboEffectSerializer
    queryset = ComboEffect.objects.all()


class ComboEffectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ComboEffectSerializer
    queryset = ComboEffect.objects.all()
