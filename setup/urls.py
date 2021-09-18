from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.cotacoes.views import CotacaoViewSet

router = routers.DefaultRouter()
router.register('cotacao', CotacaoViewSet, basename='cotacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
