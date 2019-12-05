from django.urls import path, include

from application.views import HomePageView
from rest_framework import routers

from application.api import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
] + [
    path('api/', include(router.urls)),
]
