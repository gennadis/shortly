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
        except requests.RequestException:
            raise serializers.ValidationError("URL_NOT_REACHABLE")
        if response.status_code != 200:
            raise serializers.ValidationError(
                f"URL_NOT_REACHABLE_CODE_{response.status_code}"
            )

        return value
