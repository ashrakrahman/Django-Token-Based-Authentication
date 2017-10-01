from rest_framework import serializers
from product.models import Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','product_name','product_description','product_price','company_name','company_country','product_bid')