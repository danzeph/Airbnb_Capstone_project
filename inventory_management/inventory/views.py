from rest_framework import viewsets, permissions, filters
from .models import InventoryItem
from .serializers import InventoryItemSerializer, UserSerializer
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objets.all()
    serializer_class = UserSerializer




    