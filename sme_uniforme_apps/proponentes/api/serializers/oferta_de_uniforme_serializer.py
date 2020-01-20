from rest_framework import serializers

from ...models import OfertaDeUniforme


class OfertaDeUniformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfertaDeUniforme
        fields = '__all__'


class OfertaDeUniformeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfertaDeUniforme
        exclude = ('id',)
