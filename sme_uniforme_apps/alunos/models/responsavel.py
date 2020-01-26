from django.core import validators
from django.db import models

from sme_uniforme_apps.core.models_abstracts import ModeloBase
from .aluno import Aluno


class Responsavel(ModeloBase):
    # Status Choice
    STATUS_ATUALIZADO = 'ATUALIZADO'
    STATUS_DIVERGENTE = 'DIVERGENTE'
    STATUS_ERRO = 'ERRO'

    STATUS_NOMES = {
        STATUS_ATUALIZADO: 'Atualizado',
        STATUS_DIVERGENTE: 'Divergente',
        STATUS_ERRO: 'Erro',
    }

    STATUS_CHOICES = (
        (STATUS_ATUALIZADO, STATUS_NOMES[STATUS_ATUALIZADO]),
        (STATUS_DIVERGENTE, STATUS_NOMES[STATUS_DIVERGENTE]),
        (STATUS_ERRO, STATUS_NOMES[STATUS_ERRO]),
    )

    # Vinculo Choice
    VINCULO_MAE = 'MAE'
    VINCULO_PAI = 'PAI'
    VINCULO_OUTRO = 'OUTRO'

    VINCULO_NOMES = {
        VINCULO_MAE: 'Mãe',
        VINCULO_PAI: 'Pai',
        VINCULO_OUTRO: 'Outro',
    }

    VINCULO_CHOICES = (
        (VINCULO_MAE, VINCULO_NOMES[VINCULO_MAE]),
        (VINCULO_PAI, VINCULO_NOMES[VINCULO_PAI]),
        (VINCULO_OUTRO, VINCULO_NOMES[VINCULO_OUTRO]),
    )

    cod_eol_aluno = models.ManyToManyField(Aluno, related_name='Alunos')

    vinculo = models.CharField(
        'status',
        max_length=15,
        choices=VINCULO_CHOICES,
        default=VINCULO_OUTRO
    )

    nome = models.CharField("Nome do Responsável", max_length=255, blank=True, null=True)

    cpf = models.CharField(
        "CPF", max_length=11, blank=True, null=True, unique=True, validators=[validators.MinLengthValidator(11)])

    email = models.CharField(
        "E-mail", max_length=255, validators=[validators.EmailValidator()], blank=True, null=True, default="",
        unique=True
    )
    # TODO Necessário adicionar atriburo celular. Necessário saber se será lista ou objetos.

    data_nascimento = models.DateField("Data de Nascimento")

    nome_mae = models.CharField("Nome da Mãe do Responsável", max_length=255, blank=True, null=True)

    status = models.CharField(
        'status',
        max_length=15,
        choices=STATUS_CHOICES,
        default=STATUS_ATUALIZADO
    )

    def __str__(self):
        return f"{self.nome} - {self.email}"

    class Meta:
        verbose_name = "Responsavel"
        verbose_name_plural = "Responsaveis"
