from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(type(validated_data))
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for obj in positions:
            StockProduct.objects.create(stock=stock, **obj)
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        for obj in positions:
            update_model = StockProduct.objects.filter(
                stock=instance,
                product=obj.get('product')
            )
            if update_model:
                update_model.update(**obj)
            else:
                StockProduct.objects.create(stock=stock, **obj)
        return stock
