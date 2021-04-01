from rest_framework import viewsets
from .models import Cat, Owner, Achivement
from .serializers import CatSerializer, OwnerSerializer, AchivementSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class AchivementViewSet(viewsets.ModelViewSet):
    queryset = Achivement.objects.all()
    serializer_class = AchivementSerializer
