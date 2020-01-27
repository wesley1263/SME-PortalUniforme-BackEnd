import pytest

from ..models import Aluno

pytestmark = pytest.mark.django_db


def test_instance_model(aluno):
    model = aluno
    assert isinstance(model, Aluno)
    assert model.codigo_eol
    assert model.responsavel


def test_srt_model(aluno):
    assert aluno.__str__() == '005294'


def test_meta_modelo(aluno):
    assert aluno._meta.verbose_name == 'Aluno'
    assert aluno._meta.verbose_name_plural == 'Alunos'
