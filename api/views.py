from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserAPILimitSerializer
from .models import UserAPILimit


class UserAPILimitView(APIView):
    def get(self, request):
        try:
            userId = request.query_params.get('userId')
            queryset = UserAPILimit.objects.filter(userId=userId).first()

            if not queryset:
                return Response({'message': 'User not found', 'isNewUser': True}, status=status.HTTP_200_OK)

            serializer = UserAPILimitSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserAPILimit.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        data = request.data
        userId = data.get('userId')

        if not userId:
            return Response({'message': 'userId is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserAPILimit.objects.get(userId=userId)
            user.count += 1
            user.save()
        except UserAPILimit.DoesNotExist:
            UserAPILimit.objects.create(userId=userId, count=1)

        return Response({'message': 'User count updated successfully'}, status=status.HTTP_201_CREATED)
