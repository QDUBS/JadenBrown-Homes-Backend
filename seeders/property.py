from housing.models import  Address, Category
from property.models import Property
from django.conf import settings
from account.models import Account
email = input("WHo is making a post? ")
owner = Account.objects.get(email=email)
category = Category.objects.first()
import json
BASE_DIR = settings.BASE_DIR

def seed_property():
    try:
        with open(f"{BASE_DIR}/json/properties.json", "r") as properties_file:
            propertiess = json.load(properties_file)["propertiess"]
            for property in propertiess:
                address = property.pop("address")
                address = Address.objects.create(**address)
                Property.objects.create(**property, address=address, owner=owner, category=category)

            print("DONE.....")
    except Exception as exec:
        print(exec)