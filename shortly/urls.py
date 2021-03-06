"""shortly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from api import views

urlpatterns = [
    path("admin/", admin.site.urls, name="Admin panel"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "v1/urls/",
        views.ListURLView.as_view(),
        name="List all URLs",
    ),
    path(
        "v1/urls/<str:hash>/",
        views.RetrieveUpdateURLView.as_view(),
        name="Get or Update an URL",
    ),
    path(
        "v1/shorten/",
        views.CreateURLView.as_view(),
        name="Shorten an URL",
    ),
    path(
        "<str:hash>/",
        views.redirect_from_hash,
        name="Redirect to original URL",
    ),
]
