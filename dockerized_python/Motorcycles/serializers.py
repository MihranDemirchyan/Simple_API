from Motorcycles.models import Moto
from rest_framework import serializers


class MotoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = "__all__"
