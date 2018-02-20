# Python Standard Libraries
# N/A
# Third-Party Libraries
from django.conf import settings
from django.db import models
# Custom Libraries
from .digger_model import Digger
from .item_model import Item


class Purchase(models.Model):
    """Purchases made by users

    Attributes:
        purchaser (): The digger id that purchased the item
        recipient (): The digger id that will receive the item
        item ():      The item id that will be given
    """
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name="item_of_purchase")
    purchaser = models.ForeignKey(Digger,
                                  on_delete=models.CASCADE,
                                  related_name="purchaser_of_purchase")
    recipient = models.ForeignKey(Digger,
                                  on_delete=models.CASCADE,
                                  related_name="recipient_of_purchase")

    REQUIRED_FIELDS = ["purchaser", "recipient", "item"]
