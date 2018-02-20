# Python Standard Libraries
# N/A
# Third-Party Libraries
from rest_framework import serializers
# Custom Libraries
from . import digger_model
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    password = serializers.CharField(max_length=128,
                                     min_length=8,
                                     write_only=True)

    class Meta:
        model = User
        fields = ("username", "password")

    def update(self, instance, validated_data):
        """Performs an update on a User."""

        # Passwords should not be handled with `setattr`, unlike other fields.
        # Django provides a function that handles hashing and
        # salting passwords. That means
        # we need to remove the password field from the
        # `validated_data` dictionary before iterating over it.
        password = validated_data.pop("password", None)

        for (key, value) in validated_data.items():
            # For the keys remaining in `validated_data`, we will set them on
            # the current `User` instance one at a time.
            setattr(instance, key, value)

        if password is not None:
            # `.set_password()`  handles all
            # of the security stuff that we shouldn't be concerned with.
            instance.set_password(password)

        # After everything has been updated we must explicitly save
        # the model. It's worth pointing out that `.set_password()` does not
        # save the model.
        instance.save()

        return instance
