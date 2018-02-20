# Python Standard Libraries
# N/A
# Third-Party Libraries
from django.conf import settings
import jwt
from rest_framework import authentication, exceptions
# Custom Libraries
from api.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = "bearer"

    def authenticate(self, request):
        """The `authenticate` method is called on every request regardless of
        whether the endpoint requires authentication.

        `authenticate` has two possible return values:

        1) `None` - We return `None` if we do not wish to authenticate. Usually
                    this means we know authentication will fail. An example of
                    this is when the request does not include a token in the
                    headers.

        2) `(user, token)` - We return a user/token combination when
                             authentication is successful.

                            If neither case is met, that means there's an error
                            and we do not return anything.
                            We simple raise the `AuthenticationFailed`
                            exception and let Django REST Framework
                            handle the rest.
        """
        try:
            # Should look like `Bearer 111aaa222bbb`
            auth_header = authentication.get_authorization_header(request)
            auth_header_type, auth_header_base64_encoded_value = auth_header.split()
            supported_auth_header_prefix = self.authentication_header_prefix.lower()
            # This is received a byte type. Need to convert to utf-8 for library
            auth_header_type_utf = auth_header_type.decode("utf-8")
            auth_header_value_utf = auth_header_base64_encoded_value.decode("utf-8")
            # For the sake being obvious to future me
            token = auth_header_value_utf
        except:
            return None

        # Basic error checking values for authorization
        if not (auth_header is not None and
                auth_header_type is not None and
                auth_header_base64_encoded_value is not None and
                len(auth_header_type) > 1 and
                len(auth_header_base64_encoded_value) > 1 and
                # The auth header prefix is not what we expected. Do not attempt
                # to authenticate.
                auth_header_type_utf.lower() == supported_auth_header_prefix):
            return None

        # By now, we are sure there is a *chance* that authentication will
        # succeed. We delegate the actual credentials authentication to the
        # method below.
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        Try to authenticate the given credentials. If authentication is
        successful, return the user and token. If not, throw an error.
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            error_message = "Invalid authentication. Could not decode token."
            raise exceptions.AuthenticationFailed(error_message)

        try:
            user = User.objects.get(pk=payload["id"])
        except User.DoesNotExist:
            error_message = "No user matching this token was found."
            raise exceptions.AuthenticationFailed(error_message)

        if not user.is_active:
            error_message = "This user has been deactivated."
            raise exceptions.AuthenticationFailed(error_message)

        return (user, token)
