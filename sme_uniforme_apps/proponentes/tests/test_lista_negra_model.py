import pytest

from ..models import ListaNegra


pytestmark = pytest.mark.django_db


def test_instance(proponente, lista_negra):
    assert isinstance(lista_negra, ListaNegra)
    assert lista_negra.cnpj
    assert lista_negra.razao_social




