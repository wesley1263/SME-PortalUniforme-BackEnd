from django.contrib.auth import get_user_model
from rest_framework import serializers


from ...models import Proponente


user_model = get_user_model()


class ProponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proponente
        fields = '__all__'


class ProponenteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proponente
        exclude = ('id',)


class ProponenteLookUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proponente
        fields = ('uuid', 'razao_social')
