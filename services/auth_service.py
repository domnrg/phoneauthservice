from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User
from apps.otp.models import OTPCode


def send_otp(phone: str):
    # нормализация
    phone = phone.strip().replace(" ", "")

    # получаем или создаём пользователя
    user, _ = User.objects.get_or_create(phone=phone)

    # создаём OTP
    otp = OTPCode.create_otp(user)

    # имитация отправки SMS
    print(f"OTP для {phone}: {otp.code}")

    return True


def verify_otp(phone: str, code: str):
    phone = phone.strip().replace(" ", "")

    try:
        user = User.objects.get(phone=phone)
    except User.DoesNotExist:
        return None

    otp = (
        OTPCode.objects.filter(user=user, code=code, is_used=False)
        .order_by("-created_at")
        .first()
    )

    if not otp:
        return None

    if otp.is_expired():
        return None

    otp.is_used = True
    otp.save()

    # Генерация JWT
    refresh = RefreshToken.for_user(user)

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }
