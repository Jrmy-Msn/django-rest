import logging
from django.shortcuts import render
from rest_framework.response import Response

logger = logging.getLogger(__name__)

# Create your views here.
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request):
        user = request.user
        queryset = Todo.objects.filter(user = user)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = request.user
        serializer = TodoSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(user = user)
        return Response(serializer.validated_data)
