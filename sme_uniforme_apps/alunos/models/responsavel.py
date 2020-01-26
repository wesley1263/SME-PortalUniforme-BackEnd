from django.core import validators
from django.db import models
from sme_uniforme_apps.core.models_abstracts import ModeloBase


class Responsavel(ModeloBase):
    nome = models.CharField("Nome do Responsável", max_length=255, blank=True, null=True)
    cpf = models.CharField(
        "CPF", max_length=11, blank=True, null=True, unique=True, validators=[validators.MinLengthValidator(11)])
    email = models.CharField(
        "E-mail", max_length=255, validators=[validators.EmailValidator()], blank=True, null=True, default="",
        unique=True
    )
    data_nascimento = models.DateField("Data de Nascimento")
    nome_mae = models.CharField("Nome da Mãe do Responsável", max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"

    class Meta:
        verbose_name = "Responsavel"
        verbose_name_plural = "Responsaveis"
