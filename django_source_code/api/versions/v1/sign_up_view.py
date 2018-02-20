# Python Standard Libraries
# N/A
# Third-Party Libraries
from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_401_UNAUTHORIZED
# Custom Libraries
from . import sign_up_serializer
from . import sign_up_renderer


# Documentation link
# http://www.django-rest-framework.org/api-guide/permissions/#object-level-permissions
# http://www.django-rest-framework.org/api-guide/permissions/#api-reference
@api_view(["POST"])
@permission_classes((AllowAny,))
# Response is implicity provided in the context of the renderer now
@renderer_classes((sign_up_renderer.SignUpJSONRenderer,))
def sign_up(request):
    user_serializer = sign_up_serializer.SignUpSerializer(data=request.data)

    if user_serializer.is_valid():
        try:
            user_serializer.save()

            return Response(user_serializer.data,
                            status=HTTP_201_CREATED)
        except Exception as e:
            # user already exists
            response_data = {"errors": user_serializer.errors}

            return Response(response_data,
                            status=HTTP_401_UNAUTHORIZED)
    else:
        response_data = {"errors": user_serializer.errors}
        return Response(response_data,
                        status=HTTP_401_UNAUTHORIZED)
