# Python Standard Libraries
from datetime import datetime, timedelta
# Third-Party Libraries
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from django.db import models
import jwt
# Custom Libraries
# N/A


# TODO: Figure out if this should be in the api version logic or stored here


class UserManager(BaseUserManager):
    """Extension of UserManager for custom user control."""

    def create_user(self, username=None, email=None, password=None):
        """
        Arguments:
            username
            email
            password

        Returns:
            (User): ????
        """
        if username is None:
            raise TypeError("Users must have a username.")

        if password is None:
            raise TypeError("Users must have a password.")

        if email is None:
            raise TypeError("Users must have an email address.")

        user = self.model(username=username, email=self.normalize_email(email))

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Arguments:
            username
            email
            password

        Returns:
            (User): ????
        """
        user = self.create_user(username, email, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """An extension of the User class:
    https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#django.contrib.auth.models.CustomUser

    Attributes:
        username (CharField): Unique username
        email (EmailField): An e-mail
        is_active (BooleanField):  User information cannot be deleted, only 
            deactivated
        is_staff (BooleanFiled): The `is_staff` flag is expected by Django to
            determine who can and cannot log into the Django admin site. For
            most users this flag will always be false.
        is_staff (BooleanFiled): The `is_superuser` flag is expected by Django 
        created_at (DateTimeField): A timestamp representing when this object
            was created.
        updated_at (DateTimeField): A timestamp reprensenting when this object
            was last updated.
    """
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # USERNAME_FIELD is required to specify default account association field
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    # Used to point Django to the managing class for this model
    objects = UserManager()

    def __str__(self):
        """Returns:
            String: string representation of this `User`
        """
        string = ("Username: {}"
                  " E-mail: {}").format(self.username, self.email)
        return string

    @property
    def token(self):
        """Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """Required by Django to handle emails. Usually user's first name and
        last name.

        Returns:
            string: the username instead of their full name
        """
        return self.username

    def get_short_name(self):
        """Required by Django to handle emails. Usually user's first name.


        Returns:
            string: the username instead of their name
        """
        return self.username

    def _generate_jwt_token(self):
        """Generates a JSON Web Token that stores this user's ID and has an
        expiry date set to 60 days into the future.

        Returns:
            (String): A decoded jwt token
        """
        primary_key = self.pk
        expiration_date = datetime.now() + timedelta(days=60)
        integer_expiration_date = int(expiration_date.strftime("%s"))

        jwt_data = {
            "id": primary_key,
            "exp": integer_expiration_date
        }

        token = jwt.encode(jwt_data, settings.SECRET_KEY, algorithm="HS256")

        return token.decode('utf-8')
