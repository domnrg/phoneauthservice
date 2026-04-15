import pytest
from rest_framework.test import APIClient
from apps.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_user_me_unauthorized():
    client = APIClient()
    response = client.get("/users/me/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_user_me_authorized(phone):
    user = User.objects.create(phone=phone)

    refresh = RefreshToken.for_user(user)
    access = str(refresh.access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

    response = client.get("/users/me/")

    assert response.status_code == 200
    assert response.data["phone"] == phone
