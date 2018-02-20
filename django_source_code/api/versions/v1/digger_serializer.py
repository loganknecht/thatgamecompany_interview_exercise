# Python Standard Libraries
# N/A
# Third-Party Libraries
from rest_framework import serializers
# Custom Libraries
from . import digger_model
from . import user_serializer


class DiggerSerializer(serializers.ModelSerializer):
    amount_to_dig = serializers.FloatField(write_only=True)
    depth_dug = serializers.FloatField(read_only=True)
    dubloons_in_possession = serializers.IntegerField(read_only=True)
    linked_user = user_serializer.UserSerializer(read_only=True)

    class Meta:
        model = digger_model.Digger
        fields = "__all__"
