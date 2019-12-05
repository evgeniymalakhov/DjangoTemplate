from rest_framework.viewsets import ModelViewSet

from application.serializers import UserSerializer
from application.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
