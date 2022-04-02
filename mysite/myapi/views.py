# views.py

from rest_framework import viewsets

from .serializers import HeroSerializer, StudentDetailSerializer
from .models import Hero, StudentDetail


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class StudentDetailViewSet(viewsets.ModelViewSet):
    queryset = StudentDetail.objects.all().order_by('firstname')
    serializer_class = StudentDetailSerializer
