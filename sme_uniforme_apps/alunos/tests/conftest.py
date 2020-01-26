import pytest
from model_bakery import baker


@pytest.fixture
def aluno():
    return baker.make(
        'Aluno',
        codigo_eol='005294',
    )
