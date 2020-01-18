from django.db import models
from django.core import validators

from .validators import phone_validation, cep_validation, cnpj_validation
from sme_uniforme_apps.core.models_abstracts import ModeloBase

from ...core.models.uniforme import Uniforme


class Proponente(ModeloBase):

    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins'),
    )

    cnpj = models.CharField(
        "CNPJ", max_length=20, validators=[cnpj_validation]
        , blank=True, null=True, default="", unique=True
    )
    razao_social = models.CharField("Razão Social", max_length=255, blank=True, null=True)

    end_logradouro = models.CharField(
        'endereço',
        max_length=100,
        blank=True
    )

    end_cidade = models.CharField(
        'cidade',
        max_length=80,
        blank=True
    )

    end_uf = models.CharField(
        'estado',
        max_length=2,
        blank=True,
        choices=UF_CHOICES,
        default='SP'
    )

    end_cep = models.CharField(
        'cep',
        max_length=10,
        blank=True,
        default='',
        validators=[cep_validation]
    )

    telefone = models.CharField(
        "Telefone", max_length=20, validators=[phone_validation]
        , blank=True, null=True, default=""
    )

    email = models.CharField(
        "E-mail", max_length=255, validators=[validators.EmailValidator()]
        , blank=True, null=True, default="", unique=True
    )

    responsavel = models.CharField("Responsável", max_length=255, blank=True, null=True)

    criado_em = models.DateTimeField("Criado em", editable=False, auto_now_add=True)

    def __str__(self):
        return f"{self.responsavel} - {self.email} - {self.telefone}"

    @property
    def protocolo(self):
        return f'{self.uuid.urn[9:17].upper()}'

    class Meta:
        verbose_name = "Proponente"
        verbose_name_plural = "Proponentes"


class OfertaDeUniforme(ModeloBase):
    proponente = models.ForeignKey(Proponente, on_delete=models.CASCADE, related_name='ofertas_de_uniformes')
    uniforme = models.ForeignKey(Uniforme, on_delete=models.PROTECT, related_name='proponentes')
    preco = models.DecimalField('Preço', max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.uniforme.nome} - {self.preco} - {self.proponente.razao_social}"

    class Meta:
        verbose_name = "oferta de uniforme"
        verbose_name_plural = "ofertas de uniforme"
        unique_together = ['proponente', 'uniforme']
