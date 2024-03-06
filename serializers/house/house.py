from housing.models import Address, House, Features, HouseType,Images
from rest_framework import serializers
from serializers.public.shared import AddressSerializer, CategorySerializer, OwnerReadOnlySerializer
from validators.property import validate_terms_and_condition


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("id", "image")

    def create(self, validated_data):
        house = House.objects.all()[3]
        image = Images.objects.create(**validated_data, house=house)
        return image
    


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ("id", "bedrooms", "bathrooms", "packing_space", "more_details", "balcony")


class HouseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseType
        fields = ("id","type",)



class HouseListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    type = HouseTypeSerializer()
    address = AddressSerializer()
    features = FeaturesSerializer()
    
    class Meta:
        model = House
        fields =("id", "title", "price","banner", "type","category",  "slug","address","features", "created_at", "updated_at",  )


class HouseDetailSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, source="house_images") 
    category = CategorySerializer()
    type = HouseTypeSerializer()
    features = FeaturesSerializer()
    address = AddressSerializer()
    manager = OwnerReadOnlySerializer(read_only=True, source="owner.user_profile")
    class Meta:
        model = House
        fields =("id", "title", "description", "price","banner", "type","category", "terms_and_condition", "is_available", "is_sold", "is_negotiable", "slug","manager","features", "address","images", "created_at", "updated_at",)



class HouseSearchSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    type = HouseTypeSerializer()
    features = FeaturesSerializer()
    address = AddressSerializer()
    # terms_and_condition = serializers.CharField(validaros=[    validate_terms_and_condition])
    class Meta:
        model = House
        fields =("id", "title", "description", "price","banner", "type","category", "is_available", "is_sold", "is_negotiable", "slug","terms_and_condition","features", "address", "created_at", "updated_at",)

    def validate_terms_and_condition(self, value):
        if len(value) < 100:
            raise serializers.ValidationError("Please anter a more descriptive terms and condtions")
        return value
    
    def validate_description(self, value):
        if len(value) < 200:
            raise serializers.ValidationError("Please anter a more descriptive information of the house")
    
        return value


class HouseCRUDSerializer(serializers.ModelSerializer):
    house_images = ImagesSerializer(many=True) 
    features = FeaturesSerializer()
    address = AddressSerializer()
    class Meta:
        model = House
        fields =("id", "title", "description", "price","banner", "type","category", "is_available", "is_sold", "is_negotiable", "slug","features", "address", "house_images","created_at", "updated_at",)
    
    
    def create(self, validated_data):
        address = validated_data.pop("address")
        features = validated_data.pop("features")

        # DEAL WITH IMAGES LATER
        images = validated_data.pop("house_images")
        banner = images[0]

        address = Address.objects.create(**address)

        house = House.objects.create(**validated_data, address=address, banner=banner)

        if features:
            features = Features.objects.create(**features)
            house.features=features
            house.save()
        
        for img in images:
            Images.objects.create(*img, house=house)
            
        
        return house
    
    def validate_house_images(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Invalid image format")
        if len(value) > 6:
            raise serializers.ValidationError("number of images must not be more than six")
        if len(value) <3:
            raise serializers.ValidationError("number of images must be at least three")

        return value

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

