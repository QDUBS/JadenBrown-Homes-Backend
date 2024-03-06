from rest_framework.generics import ListCreateAPIView
from housing.models import Address
from mixins.crudMixns import RetriveUpdateDestroyAPIView
from mixins.managerQueryMixins import ManagerQueryAPI
from mixins.searchMixins import SearchMixin
from property.models import Property
from serializers.property.property import PropertiesSerializer, PropertyCRUDSerializer, PropertyDetailSerializer, ProperySearchSerializer
from rest_framework.response import Response
from serializers.public.shared import AddressSerializer
from rest_framework.views import APIView


class ListPropertyView(ListCreateAPIView):
    serializer_class = PropertiesSerializer
    queryset = Property.available.select_related("category", "owner__user_profile",).order_by("-created_at")

    def get_serializer_class(self, *args, **kwargs):
        method = self.request.method
        if method == "GET":
            return PropertiesSerializer
        
        return PropertyCRUDSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
        return serializer.data


class PropertyDetailView(RetriveUpdateDestroyAPIView):
    serializer_class = PropertyDetailSerializer
    address_serializer_class = AddressSerializer
    queryset = Property.available.select_related("address", "category",  "owner__user_profile",)
    lookup_field = "slug"

    def get_serializer_class(self):
        method = self.request.method
        if method != "GET":
            return PropertyCRUDSerializer
        return super().get_serializer_class()
    
    def patch(self, request, *args, **kwargs):
        property_id = request.data.get("id")
        if not property_id:
            return Response({"msg":"no id"})
        
        property_images = request.data.pop("property_images")
        
        new_address = request.data.get("address", None)
        try:
            property = Property.objects.get(id=property_id)
            if new_address:
                try:
                    self.update_queryset = request.data.pop("address")
                    address = Address.objects.get(id=property.address.id)
                    self.update_address(instance=address, partial=True)
                except:
                    pass
            
            property_serializer = PropertyCRUDSerializer(data=request.data, instance=property, partial=True)
            property_serializer.is_valid(raise_exception=True)
            property_serializer.save()
            return Response(property_serializer.data)
        except Property.DoesNotExist:
            return Response({"Detail":"Not found"})
     

    def put(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)
    
class PropertyByMangerView(APIView):
    serializer_class = PropertiesSerializer
    def get(self, request, username):
        if not username:
            return Response({"message":"Username cannot be none"}, status=400)
        
        query = Property.objects.filter(owner__username=username).select_related("address", "category", "owner__user_profile",)
        serializer = self.serializer_class(query, many=True).data
        return Response({"count":len(serializer),"data":serializer})


class PropertySeachView(SearchMixin):
    serializer_class =ProperySearchSerializer
    queryset = Property.objects.select_related("address", "category",).order_by("-created_at")
    filterset_fields = {
        "title":["icontains", "startswith", "endswith"],
        "description":["icontains", "startswith", "endswith"],
        "address__state":["iexact"],
        "address__city":["iexact"],
        "is_negotiable":["exact"],
        "price":["exact"]
    }

class ManagerPropertyDashboardView(ManagerQueryAPI):
    serializer_class = PropertiesSerializer
    queryset = Property.objects.select_related("address", "category", "owner__user_profile",).order_by("-created_at")