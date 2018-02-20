# Python Standard Libraries
# N/A
# Third-Party Libraries
from django.contrib import admin
# Custom Libraries
from .versions import v1
from api.models import User

# Register your models here.
admin.site.register(User)
admin.site.register(v1.digger_model.Digger)
admin.site.register(v1.item_model.Item)
admin.site.register(v1.purchase_model.Purchase)
