from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics

from api.models import URL
from api.serializers import URLSerializer, URLCreationSerializer


class ListURLView(generics.ListAPIView):
    queryset = URL.objects.all().order_by("-created_at")
    serializer_class = URLSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateURLView(generics.CreateAPIView):
    serializer_class = URLCreationSerializer
    permission_classes = [permissions.IsAuthenticated]
