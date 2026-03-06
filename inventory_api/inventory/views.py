from django.shortcuts import render
from inventory.permissions import IsOwner
from inventory.models import InventoryItem, InventoryChangeHistory
from inventory.serializers import InventoryChangeHistorySerializer, InventoryItemSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


User = get_user_model()


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    ordering = ['-date_added']
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
            'category': ['iexact','exact'],
            'price': ['exact', 'gte', 'lte'],
            'quantity': ['lte'],  
        }

    search_fields = ['name','category']
    ordering_fields = ['name', 'quantity', 'price', 'date_added']

    def get_queryset(self):
        """Filter based on ownership of item"""
        if self.request.user.is_staff:
            return InventoryItem.objects.all()
        return InventoryItem.objects.filter(owner=self.request.user)


    def perform_create(self, serializer):
        """save items by a user"""
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        old_quantity = instance.quantity
        new_instance = serializer.save()
        
        # Checks if after update(patch, put) quantity changes then creeate a new history 
        if old_quantity != new_instance.quantity:
            InventoryChangeHistory.objects.create(
                item=new_instance,
                changed_by=self.request.user,
                old_quantity=old_quantity,
                new_quantity=new_instance.quantity
            )


class InventoryHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InventoryChangeHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InventoryChangeHistory.objects.all().order_by("-time_changed")
