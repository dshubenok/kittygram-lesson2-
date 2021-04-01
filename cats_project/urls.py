from django.urls import include, path
from rest_framework import routers
from cats.views import CatViewSet, OwnerViewSet, AchivementViewSet

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'achivements', AchivementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
