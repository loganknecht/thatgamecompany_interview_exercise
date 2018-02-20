# Python Standard Libraries
# N/A
# Third-Party Libraries
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Custom Libraries
from .item_model import Item
from .item_serializer import ItemSerializer


class ItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
