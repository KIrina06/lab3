from rest_framework import serializers

from .models import *


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertises
        fields = "__all__"

class RequestSerializer(serializers.ModelSerializer):
    expertise = ExpertiseSerializer(read_only=True, many=True)

    class Meta:
        model = Requests
        fields = "__all__"

