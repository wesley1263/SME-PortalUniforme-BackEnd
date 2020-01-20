import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_url_unauthorized(client):
    response = client.get('/proponentes/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_url_authorized(authenticated_client):
    response = authenticated_client.get('/proponentes/')
    assert response.status_code == status.HTTP_200_OK


def test_url_lookup(authenticated_client):
    response = authenticated_client.get('/proponentes/lookup/')
    assert response.status_code == status.HTTP_200_OK
