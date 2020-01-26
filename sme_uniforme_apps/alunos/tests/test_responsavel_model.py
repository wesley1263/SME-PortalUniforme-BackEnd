import pytest

from ..models.responsavel import Responsavel

pytestmark = pytest.mark.django_db


def test_instance_model(responsavel):
    model = responsavel
    assert isinstance(model, Responsavel)
    assert model.cod_eol_aluno
    assert model.nome
    assert model.vinculo
    assert model.cpf
    assert model.email
    assert model.data_nascimento
    assert model.nome_mae
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id
    assert model.status


def test_srt_model(responsavel):
    assert responsavel.__str__() == 'Fulano - teste@teste.com'


def test_meta_modelo(responsavel):
    assert responsavel._meta.verbose_name == 'Responsavel'
    assert responsavel._meta.verbose_name_plural == 'Responsaveis'


def test_responsavel_status_default_atualizado(responsavel):
    assert responsavel.status == Responsavel.STATUS_ATUALIZADO
