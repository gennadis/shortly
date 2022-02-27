from rest_framework import serializers

from api.models import URL


class URLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URL
        fields = ["long_url", "hash", "created_at"]


class URLCreationSerializer(serializers.HyperlinkedModelSerializer):
    short_url = serializers.ReadOnlyField(source="get_short_url")

    class Meta:
        model = URL
        fields = ["long_url", "short_url"]
