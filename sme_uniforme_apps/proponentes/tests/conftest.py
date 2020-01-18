import pytest
from model_bakery import baker


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


@pytest.fixture
def uniforme_calca():
    return baker.make('Uniforme', nome='Calça')


@pytest.fixture
def uniforme_camisa():
    return baker.make('Uniforme', nome='Camisa')


@pytest.fixture
def loja_fisica(proponente):
    return baker.make(
        'Loja',
        proponente=proponente,
        cep='27600-000',
        endereco='Rua Teste',
        bairro='Centro',
        numero='123',
        complemento='loja 1',
        telefone='(11) 4565-9876'

    )
