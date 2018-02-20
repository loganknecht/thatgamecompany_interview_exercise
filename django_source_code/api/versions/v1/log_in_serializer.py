# Python Standard Libraries
# N/A
# Third-Party Libraries
from django.contrib.auth import authenticate
from rest_framework import serializers
# Custom Libraries
# N/A


class LogInSerializer(serializers.Serializer):
    # http://www.django-rest-framework.org/api-guide/fields/#core-arguments
    username = serializers.CharField(required=True, max_length=255)
    password = serializers.CharField(required=True, max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        """This is the data that is passed to the `create` and `update` methods

        Arguments:
            data (dict): the data to validate

        Returns:
            (dict): return a dictionary of validated data
        """
        username = data.get("username", None)
        password = data.get("password", None)

        if username is None:
            error_message = "A username is required to log in."
            raise serializers.ValidationError(error_message)

        if password is None:
            error_message = "A password is required to log in."
            raise serializers.ValidationError(error_message)

        user = authenticate(username=username, password=password)

        if user is None:
            error_message = "The username and/or password were not found."
            raise serializers.ValidationError(error_message)

        # Optional - filter users who have deactivated accounts
        # if not user.is_active:
        #     error_message = "This user has been deactivated."
        #     raise serializers.ValidationError(error_message)

        data_to_return = {
            "username": user.username,
            "password": user.password,
            "token": user.token
        }

        return data_to_return
