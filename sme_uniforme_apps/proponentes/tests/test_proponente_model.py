import pytest

from django.contrib import admin
from model_bakery import baker

from ..admin import ProponenteAdmin
from ..models import Proponente

pytestmark = pytest.mark.django_db


@pytest.fixture
def proponente():
    return baker.make(
        'Proponente',
        cnpj='00.529.476/0001-14',
        razao_social='Teste',
        end_logradouro='Rua Teste, 123 apt. 101 Centro',
        end_cidade='São Paulo',
        end_uf='SP',
        end_cep='99999-000',
        telefone='(99) 99999-9999',
        email='teste@teste.com',
        responsavel='Fulano',
    )


def test_instance_model(proponente):
    model = proponente
    assert isinstance(model, Proponente)
    assert model.cnpj
    assert model.razao_social
    assert model.end_logradouro
    assert model.end_cidade
    assert model.end_uf
    assert model.end_cep
    assert model.telefone
    assert model.email
    assert model.responsavel
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id


def test_srt_model(proponente):
    assert proponente.__str__() == 'Fulano - teste@teste.com - (99) 99999-9999'


def test_meta_modelo(proponente):
    assert proponente._meta.verbose_name == 'Proponente'
    assert proponente._meta.verbose_name_plural == 'Proponentes'


def test_admin():
    model_admin = ProponenteAdmin(Proponente, admin.site)
    # pylint: disable=W0212
    assert admin.site._registry[Proponente]
    assert model_admin.list_display == ('protocolo', 'cnpj', 'razao_social', 'responsavel', 'telefone', 'email', 'alterado_em')
    assert model_admin.ordering == ('-alterado_em',)
    assert model_admin.search_fields == ('uuid', 'cnpj', 'razao_social', 'responsavel')


def test_protocolo(proponente):
    protocolo = proponente.uuid.urn[9:17].upper()
    assert proponente.protocolo == protocolo

