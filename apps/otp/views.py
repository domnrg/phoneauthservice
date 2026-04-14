from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from services.auth_service import send_otp, verify_otp

from apps.otp.serializers import SendCodeSerializer, VerifyCodeSerializer


class SendCodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SendCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]

        send_otp(phone)

        return Response({"message": "Код отправлен"}, status=status.HTTP_200_OK)


class VerifyCodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]
        code = serializer.validated_data["code"]

        tokens = verify_otp(phone, code)

        if not tokens:
            return Response(
                {"error": "Неверный или просроченный код"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response({
            "message": "Успешная авторизация",
            "tokens": tokens
        })

