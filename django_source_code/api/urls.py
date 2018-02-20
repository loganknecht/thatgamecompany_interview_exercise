# Python Standard Libraries
# N/A
# Third-Party Libraries
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
# Custom Libraries
from .versions import v1

app_name = "api"

urlpatterns = []

urlpatterns += [
    url(r'^v1/$', get_schema_view()),
    url(r"^v1/login/", v1.log_in),
    url(r"^v1/ping/", v1.ping),
    url(r"^v1/signup/", v1.sign_up),
    url(r"^v1/dig/", v1.dig),
    # Diggers
    url(r"^v1/digger/$",
        v1.DiggerViewSet.as_view({"get": "list", }),
        name="diggers"),
    url(r"^v1/digger/(?P<pk>[0-9]+)/$",
        v1.DiggerViewSet.as_view({"get": "retrieve", }),
        name="digger"),
    # Item Shop Items
    url(r"^v1/shop/item/$",
        v1.ItemViewSet.as_view({"get": "list",
                                "post": "create", }),
        name="items"),
    url(r"^v1/shop/item/(?P<pk>[0-9]+)/",
        v1.ItemViewSet.as_view({"get": "retrieve",
                                "delete": "destroy", }),
        name="item"),
    # Item Shop Purchases
    url(r"^v1/shop/purchase/$",
        v1.PurchaseViewSet.as_view({"get": "list",
                                    "post": "create", }),
        name="purchases"),
    url(r"^v1/shop/purchase/(?P<pk>[0-9]+)/",
        v1.PurchaseViewSet.as_view({"get": "retrieve",
                                    "delete": "destroy", }),
        name="purchase"),
    # Gifts (Items given)
    url(r"^v1/gift/$",
        v1.GiftViewSet.as_view({"get": "list", }),
        name="gifts"),
    # Presents (Items received)
    url(r"^v1/present/$",
        v1.PresentViewSet.as_view({"get": "list", }),
        name="presents"),
]
