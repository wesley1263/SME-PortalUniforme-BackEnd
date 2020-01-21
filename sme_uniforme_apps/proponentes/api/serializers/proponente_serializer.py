from rest_framework import serializers

from ...models import Proponente
from ...api.serializers.oferta_de_uniforme_serializer import OfertaDeUniformeSerializer
from ...api.serializers.loja_serializer import LojaSerializer
from ...api.serializers.anexo_serializer import AnexoSerializer


class ProponenteSerializer(serializers.ModelSerializer):
    ofertas_de_uniformes = OfertaDeUniformeSerializer(many=True)
    lojas = LojaSerializer(many=True)
    arquivos_anexos = serializers.ListField(
        child=AnexoSerializer()
    )

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
