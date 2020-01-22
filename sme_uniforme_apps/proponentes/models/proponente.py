from django.db import models
from django.core import validators
from django.db.models.signals import post_save
from django.dispatch import receiver

from .validators import phone_validation, cep_validation, cnpj_validation
from sme_uniforme_apps.core.models_abstracts import ModeloBase

from ...core.models.meio_de_recebimento import MeioDeRecebimento
from ..tasks import enviar_email_confirmacao_cadastro


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
        "CNPJ", max_length=20, validators=[cnpj_validation], blank=True, null=True, default="", unique=True
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
        "Telefone", max_length=20, validators=[phone_validation], blank=True, null=True, default=""
    )

    email = models.CharField(
        "E-mail", max_length=255, validators=[validators.EmailValidator()], blank=True, null=True, default="",
        unique=True
    )

    responsavel = models.CharField("Responsável", max_length=255, blank=True, null=True)

    meios_de_recebimento = models.ManyToManyField(MeioDeRecebimento, related_name='proponentes_que_aceitam')

    def __str__(self):
        return f"{self.responsavel} - {self.email} - {self.telefone}"

    @property
    def protocolo(self):
        return f'{self.uuid.urn[9:17].upper()}'

    @property
    def arquivos_anexos(self):
        return self.anexos.all()

    class Meta:
        verbose_name = "Proponente"
        verbose_name_plural = "Proponentes"


@receiver(post_save, sender=Proponente)
def contrato_post_save(instance, created, **kwargs):
    if created and instance and instance.email:
        enviar_email_confirmacao_cadastro.delay(instance.email, {'protocolo': instance.protocolo})
