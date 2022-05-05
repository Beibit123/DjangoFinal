from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render
from cafe.serializers import *
from cafe.models import *
from rest_framework.permissions import IsAuthenticated
import json
from rest_framework.decorators import action

#Soup API------------------------------------------------------
class SoupListAPIView(APIView):
    def get(self, request):
        soups = Soup.objects.all()
        serializer = SoupSerializer(soups, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SoupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SoupDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Soup.objects.get(id=pk)
        except Soup.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        soup = self.get_object(pk)
        serializer = SoupSerializer(soup)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        soup = self.get_object(pk)
        serializer = SoupSerializer(soup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        soup = self.get_object(pk)
        soup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#Dessert API---------------------------------------------------
class DessertListAPIView(APIView):
    def get(self, request):
        desserts = Dessert.objects.all()
        serializer = DessertSerializer(desserts, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = DessertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DessertDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Dessert.objects.get(id=pk)
        except Dessert.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        dessert = self.get_object(pk)
        serializer = DessertSerializer(dessert)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dessert = self.get_object(pk)
        serializer = DessertSerializer(dessert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dessert = self.get_object(pk)
        dessert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Dessert Render---------------------------------------------------
class DessertListRenderView(APIView):
    def get(self, request):
        desserts = Dessert.objects.all()
        serializer = DessertSerializer(desserts, many=True)
        return render(request, 'cafe/dessert.html', {'desserts':json.loads(json.dumps(serializer.data))})
        
    def post(self, request, format=None):
        serializer = DessertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DessertDetailRenderView(APIView):
    def get_object(self, pk):
        try:
            return Dessert.objects.get(id=pk)
        except Dessert.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        dessert = self.get_object(pk)
        serializer = DessertSerializer(dessert)
        return render(request, 'cafe/dessert.html', {'desserts':json.loads(json.dumps(serializer.data))})

    def put(self, request, pk, format=None):
        dessert = self.get_object(pk)
        serializer = DessertSerializer(dessert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'cafe/dessert.html', {'desserts':json.loads(json.dumps(serializer.data))})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dessert = self.get_object(pk)
        dessert.delete()
        desserts = Dessert.objects.all()
        serializer = DessertSerializer(desserts, many=True)
        return render(request, 'cafe/dessert.html', {'desserts':json.loads(json.dumps(serializer.data))})

#Salad------------------------------------------------------
class SaladListAPIView(APIView):
    def get(self, request):
        salads = Salad.objects.all()
        serializer = SaladSerializer(salads, many=True)
        return render(request, 'cafe/salad.html', {'salads':json.loads(json.dumps(serializer.data))})

class SaladDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Salad.objects.get(id=pk)
        except Salad.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        salad = self.get_object(pk)
        serializer = SaladSerializer(salad)
        return Response(serializer.data)

#Snack-----------------------------------------------------
class SnackListAPIView(APIView):
    def get(self, request):
        snacks = Snack.objects.all()
        serializer = SnackSerializer(snacks, many=True)
        return render(request, 'cafe/snack.html', {'snacks':json.loads(json.dumps(serializer.data))})


class SnackDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Snack.objects.get(id=pk)
        except Snack.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        snack = self.get_object(pk)
        serializer = SnackSerializer(snack)
        return Response(serializer.data)
    
#Soup Render ---------------------------------------------------------------------------------------------------    
class SoupListRenderView(APIView):
    def get(self, request):
        soups = Soup.objects.all()
        serializer = SoupSerializer(soups, many=True)
        return render(request, 'cafe/soup.html', {'soups':json.loads(json.dumps(serializer.data))})
    
    def post(self, request, format=None):
        serializer = SoupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SoupDetailRenderView(APIView):
    def get_object(self, pk):
        try:
            return Soup.objects.get(id=pk)
        except Soup.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        soup = self.get_object(pk)
        serializer = SoupSerializer(soup)
        return render(request, 'cafe/soup.html', {'soups':json.loads(json.dumps(serializer.data))})

    def put(self, request, pk, format=None):
        soup = self.get_object(pk)
        serializer = SoupSerializer(soup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            soups = Soup.objects.all()
            serializer = SoupSerializer(soups, many=True)
            return render(request, 'cafe/soup.html', {'soups':json.loads(json.dumps(serializer.data))})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        soup = self.get_object(pk)
        soup.delete()
        soups = Soup.objects.all()
        serializer = SoupSerializer(soups, many=True)
        return render(request, 'cafe/soup.html', {'soups':json.loads(json.dumps(serializer.data))})
        

#Order API------------------------------------------------------
class OrderListAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(id=pk)
        except Order.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    