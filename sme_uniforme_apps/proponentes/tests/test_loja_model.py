import pytest

from ..models import Loja


pytestmark = pytest.mark.django_db


def test_loja(proponente, loja_fisica):
    assert isinstance(loja_fisica, Loja)



