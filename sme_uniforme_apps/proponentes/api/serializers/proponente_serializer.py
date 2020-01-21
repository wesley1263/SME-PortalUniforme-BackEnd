from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ...models import Proponente, Anexo
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

    # arquivos_anexos = serializers.ListField(
    #     child=AnexoSerializer()
    # )

    def create(self, validated_data):
        arquivos_anexos = validated_data.pop('arquivos_anexos', [])
        meios_de_recebimento_list = validated_data.pop('meios_de_recebimento', [])

        proponente = Proponente.objects.create(**validated_data)

        tamanho_total_dos_arquivos = 0
        print('inicio', arquivos_anexos)
        for anexo in arquivos_anexos:
            file_size = anexo.get('arquivo').size
            tamanho_total_dos_arquivos += file_size
            if tamanho_total_dos_arquivos > 10485760:
                raise ValidationError("O tamanho total máximo dos arquivos é 10MB")
            print('Arquivo', anexo.get('arquivo').name, anexo.get('arquivo').size)
            Anexo.objects.create(proponente=proponente, arquivo=anexo.get("arquivo"))

        proponente.meios_de_recebimento.set(meios_de_recebimento_list)

        return proponente

    class Meta:
        model = Proponente
        exclude = ('id',)


class ProponenteLookUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proponente
        fields = ('uuid', 'razao_social')
