from rest_framework import serializers

from riarest.models import Appartments, Cities, Owners


class AppartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartments
        fields = '__all__'


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owners
        fields = '__all__'