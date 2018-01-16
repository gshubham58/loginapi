from rest_framework import serializers
from .models import Detail
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Detail
        fields='__all__'
class ObjectSerailzer(serializers.ModelSerializer):
    class Meta:
        model=Detail
        fields=('__all__')