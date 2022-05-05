from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from cafe.serializers import *
from cafe.models import *
import json

#Soup
class SoupListAPIView(generics.ListCreateAPIView):
    queryset = Soup.objects.all()
    serializer_class = SoupSerializer
    permission_classes = (IsAuthenticated,)


class SoupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soup.objects.all()
    serializer_class = SoupSerializer
    permission_classes = (IsAuthenticated,)

#Dessert
class DessertListAPIView(generics.ListCreateAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer
    permission_classes = (IsAuthenticated,)


class DessertDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer
    permission_classes = (IsAuthenticated,)

#Snack
class SnackListAPIView(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsAuthenticated,)


class SnackDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsAuthenticated,)

#Salads
class SaladListAPIView(generics.ListCreateAPIView):
    queryset = Salad.objects.all()
    serializer_class = SaladSerializer
    permission_classes = (IsAuthenticated,)


class SaladDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salad.objects.all()
    serializer_class = SaladSerializer
    permission_classes = (IsAuthenticated,)
