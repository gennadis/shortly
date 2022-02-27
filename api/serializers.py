from rest_framework import serializers

from api.models import URL


class URLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URL
        fields = ["long_url", "hash", "created_at"]
