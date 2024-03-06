from rest_framework import serializers
from housing.models import Address, Category


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("state","city","town","description")

    # def description


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name",)

class ContactReadOnlySerializer(serializers.Serializer):
    phone_one = serializers.CharField(read_only=True, max_length=255)
    phone_two = serializers.CharField(read_only=True, max_length=255)
    email = serializers.EmailField(read_only=True, max_length=255)

class AddressReadOnlySerializer(serializers.Serializer):
    state = serializers.CharField(read_only=True, max_length=255)
    city = serializers.CharField(read_only=True, max_length=255)
    

class OwnerReadOnlySerializer(serializers.Serializer):
    first_name = serializers.CharField(read_only=True, max_length=255)
    last_name = serializers.CharField(read_only=True, max_length=255)
    nickname = serializers.CharField(read_only=True, max_length=255)
    contact = ContactReadOnlySerializer(read_only=True)
    avata = serializers.ImageField()