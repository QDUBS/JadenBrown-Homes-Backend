from housing.models import House, HouseFeatures, Address, Category
from django.conf import settings
from account.models import Account
email = input("WHo is making a post? ")
owner = Account.objects.get(email=email)
category = Category.objects.first()
import json
BASE_DIR = settings.BASE_DIR


def seed_house():
    try:
        with open(f"{BASE_DIR}/json/house.json", "r") as house_file:
            houses = json.load(house_file)["houses"]
            for house in houses:
                address = house.pop("address")
                features = house.pop("features")

                address = Address.objects.create(**address)
                features = HouseFeatures.objects.create(**features)

                House.objects.create(**house, address=address, features=features, owner=owner, category=category)

            print("DONE.....")
    except Exception as exec:
        print(exec)


def destroyDB():
    for hf in HouseFeatures.objects.all():
        hf.delete()
    for add in Address.objects.all():
        add.delete()
    for hs in House.objects.all().delete():
        hs.delete()
    print("DATABASE DESTROYED")



command = input("What do you want to do \n")
if command.lower() == "c":
    seed_house()
    
if command.lower() == "d":
    destroyDB()
