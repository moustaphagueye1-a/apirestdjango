from api.models import Product
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status 
from .serializers import ProductSerializer1,ProductSerializer2
from rest_framework.decorators import action
class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer1
    @action(detail=False, methods=['get'], url_path='expensive', url_name='expensive')
    def expensive(self,request,*args,**kwargs):
        expensive_products=Product.objects.filter(price__gt=11)
        serializer=self.get_serializer(expensive_products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)