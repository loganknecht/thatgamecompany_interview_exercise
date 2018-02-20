# Python Standard Libraries
# N/A
# Third-Party Libraries
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
# Custom Libraries
# N/A


@api_view(["GET"])
@permission_classes((AllowAny,))
def ping(request):
    return Response({"pong": "I am alive."}, status=HTTP_200_OK)
