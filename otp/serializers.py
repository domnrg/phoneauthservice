from rest_framework import serializers

class SendSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)

class VerifySerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)
    code = serializers.CharField(max_length=6)