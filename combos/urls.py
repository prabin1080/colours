from django.urls import path

from .views import (
    ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView,
    ColourListCreateAPIView, ColourRetrieveUpdateDestroyAPIView,
    PaintListCreateAPIView, PaintRetrieveUpdateDestroyAPIView,
    ComboEffectListCreateAPIView, ComboEffectRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('project/', ProjectListCreateAPIView.as_view()),
    path('project/<int:pk>', ProjectRetrieveUpdateDestroyAPIView.as_view()),

    path('colour/', ColourListCreateAPIView.as_view()),
    path('colour/<int:pk>', ColourRetrieveUpdateDestroyAPIView.as_view()),

    path('paint/', PaintListCreateAPIView.as_view()),
    path('paint/<int:pk>', PaintRetrieveUpdateDestroyAPIView.as_view()),

    path('combo/', ComboEffectListCreateAPIView.as_view()),
    path('combo/<int:pk>', ComboEffectRetrieveUpdateDestroyAPIView.as_view()),
]
