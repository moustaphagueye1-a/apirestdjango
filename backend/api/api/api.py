from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 

from api.models import Product
from .serializers import ProductSerializer1, ProductSerializer2 # Vérifiez bien le chemin ici

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def product_api_view(request,pk=None,*args,**kwargs):
    # 1. Gestion du GET (Récupération)
    if request.method == 'GET':
        if pk is not None:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = ProductSerializer1(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        products = Product.objects.all()
        serializer = ProductSerializer1(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    # 2. Gestion du POST (Création)
    if request.method == 'POST':
        #validation d une information cote api
        data=request.data
        name=data.get('name')
       # if name in ['trump','diomaye ','sonko']:
           # return Response({'message':'Ce nom est interdit'}, status=status.HTTP_400_BAD_REQUEST   )
        serializer = ProductSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Si le serializer n'est pas valide
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 3. Gestion du PUT (Mise à jour complète)
    if request.method == 'PUT' and pk is not None:
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer1(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 4. Gestion du DELETE (Suppression)
    if request.method == 'DELETE' and pk is not None:     
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 5. Gestion du PATCH (Mise à jour partielle)
    if request.method == 'PATCH' and pk is not None:      
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer1(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)