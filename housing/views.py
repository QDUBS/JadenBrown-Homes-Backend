from housing.models import Address, House, Features, Images
from mixins.crudMixns import RetriveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from mixins.managerQueryMixins import ManagerQueryAPI
from mixins.searchMixins import SearchMixin
from serializers.house.house import HouseCRUDSerializer, HouseDetailSerializer, HouseListSerializer, HouseSearchSerializer, ImagesSerializer
from serializers.public.shared import AddressSerializer
from serializers.house.house import FeaturesSerializer 
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

class HouseListView(ListCreateAPIView):
    serializer_class = HouseListSerializer
    queryset = House.available.select_related("category", "address", "features", "type").order_by("-created_at")


    def get_serializer_class(self):
        method = self.request.method
        if method != "GET":
            return HouseCRUDSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return serializer.data
    

class HouseDetailView(RetriveUpdateDestroyAPIView):
    serializer_class = HouseDetailSerializer
    address_serializer_class = AddressSerializer
    features_serializer_class = FeaturesSerializer
    queryset = House.available.select_related("address", "category", "features", "owner__user_profile", "type")
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    def get_serializer_class(self):
        method = self.request.method
        if method != "GET":
            return HouseCRUDSerializer
        return super().get_serializer_class()


    def patch(self, request, *args, **kwargs):
        house_id = request.data["id"]
        images = request.data.get("house_images", None)
        if len(images) >=0:
            images = request.data.pop("house_images")

        try:
            house = House.objects.get(id=house_id)
            try:
                new_address = request.data.get("address", None)
                if new_address:
                    self.update_queryset = request.data.pop("address")
                    old_address = Address.objects.get(id=house.address.id)
                    self.update_address(partial=True, instance=old_address)
            except Address.DoesNotExist:
                pass

            try:
                new_features = request.data.get("features", None)
                if new_features:
                    self.update_queryset = request.data.pop("features")
                    old_features = Features.objects.get(id=house.features.id)
                    self.update_features(instance=old_features, partial=True)
            except Features.DoesNotExist:
                pass

            house_serializer = HouseCRUDSerializer(data=request.data, instance=house, partial=True)
            house_serializer.is_valid(raise_exception=True)
            house_serializer.save()
            return Response(house_serializer.data)
        except House.DoesNotExist:
            return Response({"message":f"house with {house_id} does not exist"}, 400)
        
        except Exception as exec:
            return Response(str(exec))
        
        
    def put(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)
    
class HouseByMangerView(APIView):
    serializer_class = HouseListSerializer
    def get(self, request, username):
        if not username:
            return Response({"message":"Username cannot be none"}, status=400)
        
        query = House.objects.filter(owner__username=username).select_related("address", "category", "features", "owner__user_profile", "type")
        serializer = self.serializer_class(query, many=True).data
        return Response({"count":len(serializer),"data":serializer})


class ManagerHousesDashboardView(ManagerQueryAPI):
   serializer_class = HouseListSerializer
   queryset = House.objects.select_related("address", "category", "features", "owner__user_profile", "type").order_by("-created_at")
   lookup_field = "slug"


class SearchHouseView(SearchMixin):
    serializer_class = HouseSearchSerializer
    queryset = House.available.select_related("address", "category", "features", "type")
    filterset_fields = {
        "title":["icontains", "startswith", "endswith"],
        "description":["icontains", "startswith", "endswith"],
        "type__type":["iexact"],
        "address__state":["iexact"],
        "address__city":["iexact"],
        "features__balcony":["exact"],
        "features__bathrooms":["exact"],
        "features__bedrooms":["exact"],
        "is_negotiable":["exact"],
        "price":["exact"]
    }


class ImagesView(ListCreateAPIView):
    serializer_class = ImagesSerializer
    parser_classes = [FormParser, MultiPartParser]
    queryset = Images.objects.all()