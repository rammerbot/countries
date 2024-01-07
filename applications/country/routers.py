from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, LanguageViewSet, MuseumViewSet, FloorViewSet

router = DefaultRouter()

router.register(r'countries', CountryViewSet)
router.register(r'language', LanguageViewSet)
router.register(r'floor', FloorViewSet)
router.register(r'museum', MuseumViewSet)

urlpatterns = router.urls