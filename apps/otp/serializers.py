from rest_framework import serializers


class SendCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)


class VerifyCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)
    code = serializers.CharField(max_length=6)
