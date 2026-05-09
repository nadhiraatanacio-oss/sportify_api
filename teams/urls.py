from rest_framework.routers import DefaultRouter
from .views import EquipoViewSet, JugadorViewSet

router = DefaultRouter()
router.register(r'equipos', EquipoViewSet)
router.register(r'jugadores', JugadorViewSet)

urlpatterns = router.urls