# Python Standard Libraries
# N/A
# Third-Party Libraries
from rest_framework import serializers
# Custom Libraries
from .purchase_model import Purchase
from . import digger_serializer
from . import item_serializer


class PurchaseSerializer(serializers.ModelSerializer):
    """For serializing the info of the Purchase user info?"""

    purchaser_id = serializers.IntegerField(write_only=True)
    recipient_id = serializers.IntegerField(write_only=True)
    item_id = serializers.IntegerField(write_only=True)

    purchaser = digger_serializer.DiggerSerializer(read_only=True)
    recipient = digger_serializer.DiggerSerializer(read_only=True)
    item = item_serializer.ItemSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = "__all__"
