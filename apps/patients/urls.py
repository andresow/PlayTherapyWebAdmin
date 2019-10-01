from rest_framework import routers
from .viewsets import PatientViewSet,EntityViewSet,DiagnosticViewSet,TypeDiagnosticViewSet

router = routers.SimpleRouter()
router.register('patient', PatientViewSet)
router.register('entity', EntityViewSet)
router.register('diagnostic', DiagnosticViewSet)
router.register('typeDiagnostic', TypeDiagnosticViewSet)

urlpatterns = router.urls
