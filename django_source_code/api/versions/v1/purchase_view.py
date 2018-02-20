# Python Standard Libraries
# N/A
# Third-Party Libraries
from django.conf import settings
import jwt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ModelViewSet
# Custom Libraries
from .digger_model import Digger
from .digger_view import calculate_dubloon_accrual
from .digger_view import DUBLOON_DISCOVERY_INTERVAL
from .item_model import Item
from .purchase_model import Purchase
from .purchase_serializer import PurchaseSerializer


class InsufficientDubloonsError(APIException):
    """Not enough money to complete the transaction."""
    status_code = 400
    default_detail = ("Not enough dubloons to complete this transaction.")
    default_code = "insufficient_funds"


class PurchaserAndRecipientAreSameUserError(APIException):
    """Users cannot give to themselves"""
    status_code = 400
    default_detail = ("Diggers are prohibited from purchasing items for"
                      " themselves.")
    default_code = "purchaser_cannot_be_recipient"


# Gifts are given, presents are received (eyeroll)
class GiftViewSet(ModelViewSet):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(purchaser__id=user.id)


class PresentViewSet(ModelViewSet):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(recipient_id=user.id)


class PurchaseViewSet(ModelViewSet):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
    queryset = Purchase.objects.all()

    class Meta:
        model = Purchase
        fields = "__all__"

    def create(self, request):
        purchase_serializer = PurchaseSerializer(data=request.data)
        if purchase_serializer.is_valid():
            validated_data = purchase_serializer.validated_data
            purchaser_digger_id = validated_data.get("purchaser_id")
            recipient_digger_id = validated_data.get("recipient_id")
            item_purchased_id = validated_data.get("item_id")

            purchasing_digger = Digger.objects.get(pk=purchaser_digger_id)
            recipient_digger = Digger.objects.get(pk=recipient_digger_id)
            item_purchased = Item.objects.get(pk=item_purchased_id)

            # Purchaser data tracking
            purchaser_current_dubloons = purchasing_digger.dubloons_in_possession
            purchaser_resulting_dubloons = purchaser_current_dubloons - item_purchased.shop_price

            purchasing_digger.dubloons_in_possession = purchaser_resulting_dubloons

            if purchaser_digger_id == recipient_digger_id:
                raise PurchaserAndRecipientAreSameUserError
            if purchaser_resulting_dubloons < 0:
                raise InsufficientDubloonsError

            # Recipient data tracking
            recipient_start_depth = recipient_digger.depth_dug
            recipient_amount_to_dig = item_purchased.value
            recipient_dubloons_discovered = calculate_dubloon_accrual(recipient_start_depth,
                                                                      recipient_amount_to_dig,
                                                                      DUBLOON_DISCOVERY_INTERVAL)
            recipient_digger_new_depth = recipient_start_depth + recipient_amount_to_dig
            recipient_digger_new_dubloons = recipient_digger.dubloons_in_possession + recipient_dubloons_discovered

            recipient_digger.depth_dug = recipient_digger_new_depth
            recipient_digger.dubloons_in_possession = recipient_digger_new_dubloons

            # Complete purchase
            purchase = Purchase.objects.create(item=item_purchased,
                                               purchaser=purchasing_digger,
                                               recipient=recipient_digger)

            purchasing_digger.save()
            recipient_digger.save()
            purchase.save()

            response_data = {
                "status": "Successfully purchased an item",
                "item_id": "{}".format(item_purchased_id),
                "item_price": "{}".format(item_purchased.shop_price),
                "item_value": "{}".format(recipient_amount_to_dig),
                "purchaser_user_id": "{}".format(purchaser_digger_id),
                "purchaser_start_dubloons": "{}".format(purchaser_current_dubloons),
                "purchaser_result_dubloons": "{}".format(purchaser_resulting_dubloons),
                "recipient_user_id": "{}".format(recipient_digger_id),
                "recipient_start_depth": "{}".format(recipient_start_depth),
                "recipient_end_depth": "{}".format(recipient_digger.depth_dug),
                "errors": purchase_serializer.errors
            }
            return Response(response_data,
                            status=HTTP_201_CREATED)
        else:
            response_data = {"errors": purchase_serializer.errors}
            return Response(response_data,
                            status=HTTP_401_UNAUTHORIZED)
