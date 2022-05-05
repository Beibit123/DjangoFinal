from rest_framework.decorators import api_view
import logging
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cafe.models import *
from cafe.serializers import *
import json

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'cafe/index.html')

def about(request):
    return render(request, 'cafe/about.html')

#Salad API---------------------------------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def salad_list_api(request):
    if request.method == 'GET':
        salads = Salad.objects.all()
        serializer = SaladSerializer(salads, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            salad = Salad.objects.create(name=data['name'], price=data['price'], category=data['category'], description=data['description'], url=data['url'], image=data['image'])
        except Exception as e:
            return Response({'message': str(e)})
        return Response(salad.to_json())

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def salad_item_api(request, salad_id):
    try:
        salads = Salad.objects.get(id=salad_id)
    except salads.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        return Response(salads.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        salads.name = data['name']
        salads.description = data['description']
        salads.image = data['image']
        salads.url = data['url']
        salads.price = data['price']
        salads.available = data['available']
        salads.save()
        return Response(salads.to_json())
    elif request.method == 'DELETE':
        salads.delete()
        return Response({"message": "product deleted"})

#Salad Render---------------------------------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def salad_list_render(request):
    if request.method == 'GET':
        salads = Salad.objects.all()
        serializer = SaladSerializer(salads, many=True)
        return render(request, 'cafe/salad.html', {'salads':json.loads(json.dumps(serializer.data))})
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            salad = Salad.objects.create(name=data['name'], price=data['price'])
        except Exception as e:
            return Response({'message': str(e)})

        return Response(salad.to_json())

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def salad_item_render(request, salad_id):
    try:
        salads = Salad.objects.get(id=salad_id)
    except salads.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        return Response(salads.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        salads.name = data['name']
        salads.save()
        return Response(salads.to_json())
    elif request.method == 'DELETE':
        salads.delete()
        return Response({"message": "product deleted"})
    
#Snack API -----------------------------------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def snack_list_api(request):
    if request.method == 'GET':
        snacks = Snack.objects.all()
        serializer = SnackSerializer(snacks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            snack = Snack.objects.create(name=data['name'], price=data['price'], description=data['description'], url=data['url'], image=data['image'])
        except Exception as e:
            return Response({'message': str(e)})

        return Response(snack.to_json())


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def snack_item_api(request, snack_id):
    try:
        snacks = Snack.objects.get(id=snack_id)
    except snacks.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        return Response(snacks.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        snacks.name = data['name']
        snacks.description = data['description']
        snacks.image = data['image']
        snacks.url = data['url']
        snacks.price = data['price']
        snacks.available = data['available']
        snacks.save()
        return Response(snacks.to_json())
    elif request.method == 'DELETE':
        snacks.delete()
        return Response({"message": "product deleted"})

#Snack Render-------------------------------------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def snack_list_render(request):
    if request.method == 'GET':
        snacks = Snack.objects.all()
        serializer = SnackSerializer(snacks, many=True)
        return render(request, 'cafe/snack.html', {'snacks':json.loads(json.dumps(serializer.data))})
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            snack = Snack.objects.create(name=data['name'], price=data['price'])
        except Exception as e:
            return Response({'message': str(e)})
        return Response(snack.to_json())


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def snack_item_render(request, snack_id):
    try:
        snacks = Snack.objects.get(id=snack_id)
    except snacks.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        return Response(snacks.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        snacks.name = data['name']
        snacks.save()
        return Response(snacks.to_json())
    elif request.method == 'DELETE':
        snacks.delete()
        return Response({"message": "product deleted"})

#Soup----------------------------------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def soup_list(request):
    if request.method == 'GET':
        soups = Soup.objects.all()
        serializer = SoupSerializer(soups, many=True)
        return render(request, 'cafe/soup.html', {'soups':json.loads(json.dumps(serializer.data))})
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            soup = Soup.objects.create(name=data['name'], price=data['price'])
        except Exception as e:
            return Response({'message': str(e)})

        return Response(soup.to_json())


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def soup_item(request, soup_id):
    try:
        soups = Soup.objects.get(id=soup_id)
    except soups.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        return Response(soups.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        soups.name = data['name']
        soups.save()
        return Response(soups.to_json())
    elif request.method == 'DELETE':
        soups.delete()
        return Response({"message": "product deleted"})
    
#Dessert
@api_view(['GET', 'POST'])
def dessert_list(request):
    if request.method == 'GET':
        desserts = Dessert.objects.all()
        serializer = SaladSerializer(desserts, many=True)
        return render(request, 'cafe/dessert.html', {'desserts':json.loads(json.dumps(serializer.data))})
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            dessert = Salad.objects.create(name=data['name'], price=data['price'])
        except Exception as e:
            return Response({'message': str(e)})

        return Response(dessert.to_json())


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def dessert_item(request, dessert_id):
    try:
        desserts = Dessert.objects.get(id=dessert_id)
    except desserts.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        return Response(desserts.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        desserts.name = data['name']
        desserts.save()
        return Response(desserts.to_json())
    elif request.method == 'DELETE':
        desserts.delete()
        return Response({"message": "product deleted"})