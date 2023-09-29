from rest_framework.serializers import ModelSerializer
from .models import UserAPILimit, UserSubscription


class UserAPILimitSerializer(ModelSerializer):
    class Meta:
        model = UserAPILimit
        fields = ['userId', 'count']


class UserSubscriptionSerializer(ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = ['userId', 'stripeCustomerId', 'stripeSubscriptionId', 'stripePriceId', 'stripeCurrentPeriodStart', 'stripeCurrentPeriodEnd']
