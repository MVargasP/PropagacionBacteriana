from django.urls import path
from rest_framework.routers import DefaultRouter
from bacteria.api.views import BacterialStrainViewSet, BacterialPopulationView

router = DefaultRouter()
router.register(r'strains', BacterialStrainViewSet)

urlpatterns = router.urls + [
    path('population/', BacterialPopulationView.as_view()),
]
