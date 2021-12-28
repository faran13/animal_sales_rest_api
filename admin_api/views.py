
from re import T
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import animal
from .seralizers import animalSeralizer

@api_view(['GET'])
def apiOverview(request):
    list = {
        'list' : '/get-animals/',
        'detail-view' : '/detail-view/<str:pk>/',
        'create-animal' : '/create-animal/',
        'delete-animal' : '/delete-animal/<str:pk>',
        'update-animal':'/update-animal<str:pk>',
     }
    return Response(list) 

@api_view(['GET'])
def getAnimals(request):
    getAllAnimals = animal.objects.all()
    serial = animalSeralizer(getAllAnimals, many = True)
    return Response(serial.data)

@api_view(['GET'])
def getSingleAnimal(request, id):
    getAllAnimals = animal.objects.get(id = id)
    serial = animalSeralizer(getAllAnimals, many = False)
    return Response(serial.data)


@api_view(['POST'])
def createAnimal(request):
    serial = animalSeralizer(data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

@api_view(['POST'])
def updateAnimal(request, id):
    getSingleItem = animal.objects.get(id = id)
    serial = animalSeralizer(instance = getSingleItem,data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

@api_view(['DELETE'])
def deleteAnimal(request, id):
    getSingleItem = animal.objects.get(id = id)
    getSingleItem.delete()
    return Response('Animal deleted successfully')