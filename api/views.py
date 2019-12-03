from rest_framework.viewsets import ModelViewSet

from api.serializers import UserSerializer
from application.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
