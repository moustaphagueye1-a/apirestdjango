from api.models import Product
from rest_framework import serializers
class ProductSerializer1(serializers.ModelSerializer):
    price_in_euros=serializers.SerializerMethodField()
    description_in_euros=serializers.SerializerMethodField()
    detail_link=serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields = '__all__'
        
    def get_price_in_euros(self,obj):
        return obj.get_price_in_euros()
    def get_description_in_euros(self,obj):
        return obj.get_description_in_euros()
    def get_detail_link(self,obj):
         return f'/api/product/{obj.id}/'
        
    def validate_name(self,value):
            if value in ['trump','diomaye','sonko']:
                raise serializers.ValidationError('Ce nom est interdit')
            return value
class ProductSerializer2(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    price=serializers.FloatField()
    description=serializers.CharField()
   
