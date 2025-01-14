from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,BookInventoryViewSet,BookTransactionViewSet

# Create a router and register the UserLoginViewSet
router = DefaultRouter()
router.register(r'user', UserViewSet),
router.register(r'inventory', BookInventoryViewSet),
router.register(r'transaction', BookTransactionViewSet),

urlpatterns = [
    path('apis/', include(router.urls)),
]