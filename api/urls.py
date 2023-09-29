from django.urls import path
from .views import UserAPILimitView, UserSubscriptionView

urlpatterns = [
    path('user-api-limit/', UserAPILimitView.as_view(), name='user-api-limit'),
    path('user-subscription/', UserSubscriptionView.as_view(), name='user-subscription'),
]
