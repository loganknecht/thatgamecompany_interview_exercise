# Python Standard Libraries
import base64
# Third-Party Libraries
from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
# Custom Libraries
from . import log_in_serializer


@api_view(["POST"])
@permission_classes((AllowAny,))
def log_in(request):
    auth_header = request.META['HTTP_AUTHORIZATION']
    basic_label, base_64_encoded_credentials = auth_header.split(' ')
    decoded_credentials = base64.b64decode(base_64_encoded_credentials)
    decoded_credentials_utf8 = decoded_credentials.decode("utf-8")
    username, password = decoded_credentials_utf8.split(':')

    user_log_in_data = {
        "username": username,
        "password": password,
    }

    # only validation is a concern, no need to save
    # serializer = log_in_serializer.LogInSerializer(data=user)
    serializer = log_in_serializer.LogInSerializer(data=user_log_in_data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data, status=HTTP_200_OK)
