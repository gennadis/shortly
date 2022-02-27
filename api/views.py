from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from api.models import URL
from api.serializers import URLSerializer


class URLViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows URLs to be viewed or edited.
    """

    queryset = URL.objects.all().order_by("-created_at")
    serializer_class = URLSerializer
    permission_classes = [permissions.IsAuthenticated]
