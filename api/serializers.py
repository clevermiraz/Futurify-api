from rest_framework.serializers import ModelSerializer
from .models import UserAPILimit


class UserAPILimitSerializer(ModelSerializer):
    class Meta:
        model = UserAPILimit
        fields = ['userId', 'count']
