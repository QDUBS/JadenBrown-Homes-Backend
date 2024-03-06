from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()

    def validate_password(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("password should be at least 6 charaters")
        if str(value).startswith("1234"):
            raise serializers.ValidationError("password is too common")
        return value