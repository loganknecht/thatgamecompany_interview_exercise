# Python Standard Libraries
# N/A
# Third-Party Libraries
from django.db import models
# Custom Libraries


class Item(models.Model):
    """Items that to be given to people.

    Attributes:
        short_description (): TODO
        long_description ():  TODO
        name ():              TODO
        value ():             TODO
    """
    name = models.CharField("Item_Name", max_length=30)
    short_description = models.CharField("Short_Description",
                                         default="",
                                         max_length=120)
    long_description = models.CharField("Long_Description",
                                        default="",
                                        max_length=500)
    value = models.FloatField("Value")
    shop_price = models.IntegerField("Shop_Price", default=1)

    REQUIRED_FIELDS = ["name", "shop_price", "value", ]
