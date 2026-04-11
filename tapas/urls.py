from django.urls import path

from .views import TapaViewSet, TapasViewSet, LozasViewSet, TextosViewSet


urlpatterns = [
    path('tapas', TapasViewSet.as_view(), name='tapas'),
    path('tapa/<int:pk>', TapaViewSet.as_view(), name='tapa'),
    path('lozas', LozasViewSet.as_view(), name='lozas'),
    path('textos', TextosViewSet.as_view(), name='textos')
]
