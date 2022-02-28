import requests
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

    def validate_long_url(self, value):
        try:
            response = requests.head(url=value)
        except requests.RequestException as e:
            raise serializers.ValidationError("URL is not reachable.")
        if response.status_code != 200:
            raise serializers.ValidationError(
                f"URL is not reachable. Status code: {response.status_code}"
            )

        return value
