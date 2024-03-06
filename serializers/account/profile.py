from account.models import AccountProfile, Contact, Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("state", "city", "street", "description",)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("email", "phone_one", "phone_two", )

class AccountProfileSerializer(serializers.ModelSerializer):
    is_agent = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    contact = ContactSerializer()
    address = AddressSerializer()
    class Meta:
        model = AccountProfile
        fields =( "user","contact", "address", "first_name", "last_name", "nickname", "is_agent", "image_url","slug",)

    def get_is_agent(self, obj):
        try:
            return obj.accout_type == "agent"
        except:
            return False
    
    def get_user(self, obj):
        try:
            user = {
                "id":obj.user.id,
                "email":obj.user.email
            }
            return user
        except:
            return {}
    

    def create(self, validated_data):
        address = validated_data.pop("address")
        contact = validated_data.pop("contact")
        request = self.context.get("request", None)
        email = None

        if "email" not in contact.keys():
            if request:
                email = request.user.email
                contact = Contact.objects.create(**contact, email=email)
        else:
            contact = Contact.objects.create(**contact)

        address = Address.objects.create(**address)

        profile = AccountProfile.objects.create(**validated_data, contact=contact, address=address)
        return profile

