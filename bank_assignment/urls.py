

from django.contrib import admin
from django.urls import path, include
from .routers import router
from bankapi import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('bankapi.urls')),
]


