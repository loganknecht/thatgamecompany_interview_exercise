"""thatgamecompany_interview_exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Python Standard Libraries
# N/A
# Third-Party Libraries
from django.conf.urls import url, include
from django.contrib import admin
# Custom Libraries
from api import urls as api_urls

urlpatterns = [
    url(r'^api/', include(api_urls, namespace="api")),
    url(r'admin/', admin.site.urls),
]
