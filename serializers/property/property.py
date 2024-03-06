from rest_framework import serializers
from housing.models import Address
from property.models import Property, Images
from serializers.house.house import ImagesSerializer
from serializers.public.shared import AddressReadOnlySerializer, AddressSerializer, CategorySerializer, OwnerReadOnlySerializer


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("id", "image")


class PropertiesSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Property
        fields = ("id", "title", "description", "price","banner","slug", "address", "category",)
    def get_address(self, obj):
        try:
            return f'{obj.address.city}, {obj.address.state}'
        except:
            return ""

    def get_category(self,obj):
        try:
            return obj.category.name
        except:
            return ""


class PropertyDetailSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, source="property_images") 
    category = CategorySerializer()
    address = AddressReadOnlySerializer()
    manager = OwnerReadOnlySerializer(read_only=True, source="owner.user_profile")
    class Meta:
        model = Property
        fields =("id", "title", "description", "price","banner","category", "is_available", "is_sold", "is_negotiable", "slug","manager", "address","images", "created_at", "updated_at",)


class ProperySearchSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    address = AddressReadOnlySerializer()
    class Meta:
        model = Property
        fields =("id", "title", "description", "price","banner","category", "is_available", "is_sold", "is_negotiable", "slug", "address", "created_at", "updated_at",)


class PropertyCRUDSerializer(serializers.ModelSerializer):
    property_images = ImagesSerializer(many=True) 
    address = AddressSerializer()
    class Meta:
        model = Property
        fields =("title", "description", "price","banner", "is_available", "is_sold", "is_negotiable",  "address","property_images", )


    def create(self, validated_data):
        address = validated_data.pop("address")
        images = validated_data.pop("property_images")
        print(address)
        address = Address.objects.create(**address)
        property = Property.objects.create(**validated_data, address=address)

        if len(images) > 0:
            for image in images:
                Images.objects.create(**image, property=property)
            
        
        return property

