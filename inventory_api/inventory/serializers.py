from rest_framework import serializers
from .models import InventoryChangeHistory, InventoryItem


class InventoryItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.useername")

    class Meta:
        model = InventoryItem
        fields = "__all__"

    
    def validate(self, data):
        """validates quantity and price even though models handles that"""
        quantity = data.get('quantity')
        price = data.get('price')
        if price and price <=0:
            raise serializers.ValidationError("Price cannot be negative")
        if quantity and quantity <= 0:
            serializers

    
class InventoryChangeHistorySerializer(serializers.ModelSerializer):
    """ iventory change log"""
    item_name = serializers.ReadOnlyField(source="item.name")
    changed_by = serializers.ReadOnlyField(source="changed_by.username")

    class Meta:
        model = InventoryChangeHistory
        fields = "__all__"