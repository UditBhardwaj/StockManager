from rest_framework import serializers

from inventoryapp.models import Stock,Sales

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity','price']
        # fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['issue_by', 'issue_quantity', 'phone_number', 'price_per_product']
