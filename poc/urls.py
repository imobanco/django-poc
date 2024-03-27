"""poc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path

from .view import async_sleep, sync_sleep, AsyncView

urlpatterns = [
    path("", sync_sleep, name="sync_sleep_index"),
    path("sync_sleep/", sync_sleep, name="sync_sleep"),
    path("async_sleep/", async_sleep, name="async_sleep"),
    path("async_view/", AsyncView.as_view())
]
