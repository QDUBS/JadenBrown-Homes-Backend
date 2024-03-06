from rest_framework.generics import RetrieveAPIView, DestroyAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions
from permissions.base import PropertyManagerPermission

class ListCreateDestroy(ListAPIView, CreateAPIView,DestroyAPIView):
    pass


class CustomUpdateAPI():
    address_serializer_class = None
    features_serializer_class = None
    update_queryset = None

    def checkInstance(self,instance, message):
         if not instance:
            raise Exception({"message":message})
         
         
         
    def update_address(self,instance=None, partial=False):
        self.checkInstance(instance, "An instance is address is required")
        if (self.address_serializer_class and self.update_queryset):
            address_serializer = self.address_serializer_class(data=self.update_queryset, instance=instance, partial=partial)
            address_serializer.is_valid(raise_exception=True)
            address_serializer.save()
        else:
            pass
        
    def update_features(self, instance=None, partial=False):
        self.checkInstance(instance, message="An instance is features is required")
        if (self.features_serializer_class and self.update_queryset):
            feautures_serializer = self.features_serializer_class(data=self.update_queryset, instance=instance, partial=partial)
            feautures_serializer.is_valid(raise_exception=True)
            feautures_serializer.save()

        else:
            pass


class RetriveUpdateDestroyAPIView(
    RetrieveAPIView, 
    DestroyAPIView, 
    UpdateAPIView,
    CustomUpdateAPI):
    parser_classes  = [MultiPartParser, FormParser]
    permission_classes =[permissions.IsAuthenticatedOrReadOnly, PropertyManagerPermission]
    
