# Python Standard Libraries
# N/A
# Third-Party Libraries
from django.conf import settings
from django.db import models
# Custom Libraries


class Digger(models.Model):
    """The context of the user as a `player`.

    Players in this world are `diggers`.

    Attributes:
        linked_user: The foreign key id of the unique user name
        depth_dug: The distinct value (distance) that a player has dug
    """
    linked_user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE,
                                       related_name="owner_of_digger")
    depth_dug = models.FloatField("Depth_Dug", default=0)
    dubloons_in_possession = models.IntegerField("Dubloons_In_Possession",
                                                 default=0)
