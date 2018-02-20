# Python Standard Libraries
import base64
# Third-Party Libraries
from django.conf import settings
from django.db import IntegrityError
import jwt
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ModelViewSet
# Custom Libraries
from .digger_model import Digger
from .digger_serializer import DiggerSerializer


# Need to consider this with more nuance (maybe)
DUBLOON_DISCOVERY_INTERVAL = 5
DUBLOON_DISCOVERY_AMOUNT = 1


class DiggerViewSet(ModelViewSet):
    serializer_class = DiggerSerializer
    permission_classes = [IsAuthenticated]
    queryset = Digger.objects.all()

    class Meta:
        model = Digger
        fields = "__all__"


# Documentation link
# http://www.django-rest-framework.org/api-guide/permissions/#object-level-permissions
# http://www.django-rest-framework.org/api-guide/permissions/#api-reference
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def dig(request):
    digger_data = DiggerSerializer(data=request.data)

    if digger_data.is_valid():
        validated_data = digger_data.validated_data
        amount_to_dig = validated_data.get("amount_to_dig", None)

        user = request.user
        user_id = user.id

        digger = Digger.objects.get(linked_user__id=user_id)

        start_depth = digger.depth_dug
        dubloons_discovered = calculate_dubloon_accrual(start_depth,
                                                        amount_to_dig,
                                                        DUBLOON_DISCOVERY_INTERVAL)

        new_depth = digger.depth_dug + amount_to_dig
        new_dubloon_possession_count = digger.dubloons_in_possession + dubloons_discovered

        digger.depth_dug = new_depth
        digger.dubloons_in_possession = new_dubloon_possession_count

        # TODO: hook up logging and output this
        # (" Dig operation performed "
        #     " user_id: {}"
        #     " start_depth: {}"
        #     " new_depth: {}"
        #     " dubloons_discovered: {}".format(user_id,
        #                                       start_depth,
        #                                       new_depth,
        #                                       dubloons_discovered))

        digger.save()

        response_data = {
            "status": "Dig successful",
            "initial_depth": start_depth,
            "new_depth": digger.depth_dug,
            "depth_dug": amount_to_dig,
            "dubloons_discovered": dubloons_discovered
        }
        return Response(response_data,
                        status=HTTP_200_OK)
    else:
        response_data = {"errors": digger_data.errors}
        return Response(response_data,
                        status=HTTP_401_UNAUTHORIZED)


def calculate_dubloon_accrual(start_depth, amount_to_dig, dubloon_discovery_interval):
    """Helper function to calculate the amount of dubloons discovered during a
    digging operation.

    Note: This calculation ignores any fractional amount of distance

    Arguments:
        start_depth (Float): the depth of the digger before digging
        end_depth (Float): the depth of the digger after digging
        dubloon_discovery_interval (Float): Assumes that every amount of this,
            when caluclated in conjunction with the interval will provide a
            digging dubloon
        calculation_origin (Float): The offset to calculate intervals from

    Returns:
        (integer): The number of dubloons that would be found in this digging
            scenario
    """
    # TODO: Make this "elegant"
    dubloons_accrued = 0
    current_dubloon_progress = start_depth % dubloon_discovery_interval
    amount_until_next_dubloon = dubloon_discovery_interval - current_dubloon_progress

    current_depth = start_depth
    for i in range(int(amount_to_dig)):
        amount_to_dig -= 1
        amount_until_next_dubloon -= 1
        current_depth += 1

        if amount_until_next_dubloon == 0:
            dubloons_accrued += DUBLOON_DISCOVERY_AMOUNT
            amount_until_next_dubloon = dubloon_discovery_interval

    return dubloons_accrued
