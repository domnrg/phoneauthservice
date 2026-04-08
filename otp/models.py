from django.db import models
from django.utils import timezone
from datetime import timedelta
import random

from users.models import User


class OTPCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="otp_codes")
    code = models.CharField(max_length=6, verbose_name="Код подтверждения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    expires_at = models.DateTimeField(verbose_name="Время истечения")
    is_used = models.BooleanField(default=False, verbose_name="Использован")

    class Meta:
        verbose_name = "OTP код"
        verbose_name_plural = "OTP коды"

    def __str__(self):
        return f"{self.user.phone} — {self.code}"

    # Метод для проверки срока действия
    def is_expired(self):
        return timezone.now() > self.expires_at

    # Генерация случайного кода
    @staticmethod
    def generate_code():
        return f"{random.randint(100000, 999999)}"

    # Создание нового OTP
    @classmethod
    def create_otp(cls, user, validity_minutes=5):
        code = cls.generate_code()
        expires_at = timezone.now() + timedelta(minutes=validity_minutes)
        otp = cls.objects.create(user=user, code=code, expires_at=expires_at)
        return otp
