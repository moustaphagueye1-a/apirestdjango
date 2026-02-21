from django.urls import path
from api.api.viewset import ProductViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
### DefaultRouter ajoute est  utulise pour les operations CRUD (Create, Read, Update, Delete) et inclut automatiquement une route pour la page d'accueil de l'API.
### SimpleRouter est utilisé pour les opérations de lecture (Read) uniquement et n'inclut pas de route pour la page d'accueil de l'API.
router = DefaultRouter()
router.register('v1/product', ProductViewSet, basename='product')
urlpatterns = router.urls   