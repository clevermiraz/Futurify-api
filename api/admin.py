from django.contrib import admin
from .models import UserAPILimit, UserSubscription


@admin.register(UserAPILimit)
class UserAPILimitAdmin(admin.ModelAdmin):
    list_display = ['userId', 'count', 'created_at']
    list_filter = ['userId', 'count', 'created_at', 'updated_at']
    search_fields = ['userId', 'count']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 10


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['userId', 'stripeCustomerId', 'stripePriceId', 'stripeCurrentPeriodEnd']
    search_fields = ['userId', 'stripeCustomerId']
    list_per_page = 10
