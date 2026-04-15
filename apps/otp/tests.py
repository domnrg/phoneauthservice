import pytest
from apps.users.models import User
from apps.otp.models import OTPCode


@pytest.mark.django_db
def test_send_code(client, phone):
    response = client.post("/auth/send-code/", {"phone": phone})

    assert response.status_code == 200
    assert User.objects.filter(phone=phone).exists()
    assert OTPCode.objects.filter(user__phone=phone).exists()


@pytest.mark.django_db
def test_verify_code_success(client, phone):
    # 1. отправляем код
    client.post("/auth/send-code/", {"phone": phone})

    otp = OTPCode.objects.filter(user__phone=phone).last()

    # 2. проверяем код
    response = client.post(
        "/auth/verify-code/",
        {"phone": phone, "code": otp.code},
    )

    assert response.status_code == 200
    assert "access" in response.data["tokens"]
    assert "refresh" in response.data["tokens"]


@pytest.mark.django_db
def test_verify_code_fail(client, phone):
    client.post("/auth/send-code/", {"phone": phone})

    response = client.post(
        "/auth/verify-code/",
        {"phone": phone, "code": "000000"},
    )

    assert response.status_code == 400
    assert "error" in response.data
