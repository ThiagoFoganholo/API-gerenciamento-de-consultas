from django.shortcuts import render
from .models import Consulta, Profissional
from .serializers import ProfissionalSerializer, ConsultaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def Profissional_list(request):
    if request.method == 'GET':
        profissional = Profissional.objects.all()
        serializer = ProfissionalSerializer(profissional, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProfissionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Consulta_list(request):
    if request.method == 'GET':
        consulta = Consulta.objects.all()
        serializer = ConsultaSerializer(consulta, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ConsultaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Profissional_detail(request, id):
    try:
        profissional = Profissional.objects.get(pk=id)
    except Profissional.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProfissionalSerializer(profissional)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProfissionalSerializer(profissional, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        profissional.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def Consulta_detail(request, id):
    try:
        consulta = Consulta.objects.get(pk=id)
    except Consulta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ConsultaSerializer(consulta)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ConsultaSerializer(consulta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        consulta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
