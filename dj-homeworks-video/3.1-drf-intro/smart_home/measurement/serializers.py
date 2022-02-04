from rest_framework import serializers

from . import models
from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        return models.Sensor.objects.create(name=name, description=description)

    def update(self, instance, validated_data):
        name = validated_data.get('name', instance.name)
        description = validated_data.get('description', instance.description)
        instance.name = name
        instance.description = description
        instance.save()
        return instance


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
