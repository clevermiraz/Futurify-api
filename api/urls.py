from django.urls import path
from .views import UserAPILimitView

urlpatterns = [
    path('user-api-limit/', UserAPILimitView.as_view(), name='user-api-limit'),
]
