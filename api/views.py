from django.shortcuts import get_object_or_404, redirect
from rest_framework import permissions
from rest_framework import generics

from api.models import URL
from api.serializers import URLSerializer, URLCreationSerializer


class CreateURLView(generics.CreateAPIView):
    """Endpoint to shorten an URL: /v1/shorten/"""

    serializer_class = URLCreationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListURLView(generics.ListAPIView):
    """Endpoint to list all URLs: /v1/urls/"""

    queryset = URL.objects.all().order_by("-created_at")
    serializer_class = URLSerializer
    permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateURLView(generics.RetrieveUpdateAPIView):
    """Endpoint to GET or PATCH an URL: /v1/urls/{hash}/"""

    queryset = URL.objects.all()
    lookup_field = "hash"
    serializer_class = URLSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "patch", "options"]


def redirect_from_hash(request, hash):
    url = get_object_or_404(URL, hash=hash)
    return redirect(url.long_url)
