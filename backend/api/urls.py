from django.urls import path,include
from api.api.api import product_api_view
from api.api.mixins import ProductListApiView, ProductDetailApiView,ProductCreateApiView,ProductUpdateApiView,ProductDeleteApiView, CombineApiViewset
from .views import home

urlpatterns = [
    path('',home,name='home'),
    path('product/',product_api_view,name='product_api_view'),
    path('product/<int:pk>/',product_api_view,name='product_api_view'),
    path('',include('api.routers')) ,
    path('v2/product-list/', ProductListApiView.as_view(),name='product_api_view' ),
    path('v2/product-detail/<int:pk>/', ProductDetailApiView.as_view(),name='product_detail_api_view' ),
    path('v2/product-create/', ProductCreateApiView.as_view(),name='product_create_api_view' ),
    path('v2/product-update/<int:pk>/', ProductUpdateApiView.as_view(),name='product_update_api_view' ),
    path('v2/product-delete/<int:pk>/', ProductDeleteApiView.as_view(),name='product_delete_api_view' ),
    path('v2/product-combine/', CombineApiViewset.as_view(),name='product_combine_api_view' ),
    path('v2/product-combine/<int:pk>/', CombineApiViewset.as_view(),name='product_combine_api_view' ),
    

    
]