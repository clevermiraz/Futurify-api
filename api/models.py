from django.db import models


class UserAPILimit(models.Model):
    userId = models.CharField(max_length=255, unique=True)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.userId} - {self.count}'


class UserSubscription(models.Model):
    userId = models.CharField(max_length=255, unique=True)
    stripeCustomerId = models.CharField(max_length=255, unique=True, null=True, blank=True)
    stripeSubscriptionId = models.CharField(max_length=255, unique=True, null=True, blank=True)
    stripePriceId = models.CharField(max_length=255, null=True, blank=True)
    stripeCurrentPeriodStart = models.DateTimeField(null=True, blank=True)
    stripeCurrentPeriodEnd = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.userId} - {self.stripeCustomerId}'
