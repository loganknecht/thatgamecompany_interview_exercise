# Python Standard Libraries
# N/A
# Third-Party Libraries
from rest_framework import serializers
# Custom Libraries
from api.models import User
from . import digger_model


class SignUpSerializer(serializers.ModelSerializer):
    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(max_length=128,
                                     min_length=8,
                                     write_only=True)

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        # Pretty sure this should be using the setings AUTH_USER_MODEL???
        # model = settings.AUTH_USER_MODEL
        model = User
        fields = "__all__"

    def create(self, validated_data):
        new_user = User.objects.create_user(email=validated_data["email"],
                                            password=validated_data["password"],
                                            username=validated_data["username"])
        # Digger is created to connect the play context with the user context
        new_digger = digger_model.Digger.objects.create(linked_user=new_user)

        return new_user
