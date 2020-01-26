from django.core import validators
from django.db import models
from sme_uniforme_apps.core.models_abstracts import ModeloBase


class Aluno(ModeloBase):
    codigo_eol = models.CharField(
        "Código EOL do Aluno", max_length=6, unique=True, validators=[validators.MinLengthValidator(6)])

    def __str__(self):
        return {self.codigo_eol}

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
