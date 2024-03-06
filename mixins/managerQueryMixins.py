from mixins.crudMixns import RetriveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from permissions.agent import IsAgentPermission
from permissions.base import PropertyManagerPermission


class ManagerQueryAPI(ListAPIView):
    permission_classes = [ permissions.IsAuthenticated, IsAgentPermission, PropertyManagerPermission]
    
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)