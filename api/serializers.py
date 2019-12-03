from rest_framework.serializers import ModelSerializer

from application.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
