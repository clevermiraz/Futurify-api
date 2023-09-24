from django.contrib import admin
from .models import UserAPILimit


@admin.register(UserAPILimit)
class UserAPILimitAdmin(admin.ModelAdmin):
    list_display = ['userId', 'count', 'created_at']
    list_filter = ['userId', 'count', 'created_at', 'updated_at']
    search_fields = ['userId', 'count']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 10
