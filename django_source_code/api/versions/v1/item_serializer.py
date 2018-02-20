# Python Standard Libraries
# N/A
# Third-Party Libraries
from rest_framework import serializers
# Custom Libraries
from .item_model import Item


class ItemSerializer(serializers.ModelSerializer):
    """TODO."""

    class Meta:
        model = Item
        fields = "__all__"
