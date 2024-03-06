from rest_framework import serializers

from account.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "email", "password")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Account.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def validate_password(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("password should be at least 6 charaters")
        if str(value).startswith("1234"):
            raise serializers.ValidationError("password is too common")
        return value