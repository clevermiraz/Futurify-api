from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserAPILimitSerializer, UserSubscriptionSerializer
from .models import UserAPILimit, UserSubscription


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


class UserSubscriptionView(APIView):
    def get(self, request):
        try:
            userId = request.query_params.get('userId')
            queryset = UserSubscription.objects.filter(userId=userId).first()

            if not queryset:
                return Response({'message': 'User not found', 'isNewUser': True}, status=status.HTTP_200_OK)

            serializer = UserSubscriptionSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except UserSubscription.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        data = request.data
        userId = data.get('userId')
        stripeSubscriptionId = data.get('stripeSubscriptionId')
        stripeCustomerId = data.get('stripeCustomerId')
        stripePriceId = data.get('stripePriceId')
        stripeCurrentPeriodStart = data.get('stripeCurrentPeriodStart')
        stripeCurrentPeriodEnd = data.get('stripeCurrentPeriodEnd')

        if not userId and stripeCustomerId:
            return Response({'message': 'userId and stripeCustomerId is Required'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            userSubscription = UserSubscription.objects.get(stripeSubscriptionId=stripeSubscriptionId)

            userSubscription.stripePriceId = stripePriceId
            userSubscription.stripeCurrentPeriodStart = stripeCurrentPeriodStart
            userSubscription.stripeCurrentPeriodEnd = stripeCurrentPeriodEnd
            userSubscription.save()
            return Response({'message': 'UserSubscription Updated Successfully'}, status=status.HTTP_200_OK)

        except UserSubscription.DoesNotExist:
            userSubscription = UserSubscription()
            userSubscription.userId = userId
            userSubscription.stripeSubscriptionId = stripeSubscriptionId
            userSubscription.stripeCustomerId = stripeCustomerId
            userSubscription.stripePriceId = stripePriceId
            userSubscription.stripeCurrentPeriodStart = stripeCurrentPeriodStart
            userSubscription.stripeCurrentPeriodEnd = stripeCurrentPeriodEnd
            userSubscription.save()

            return Response({'message': 'UserSubscription Created Successfully'}, status=status.HTTP_201_CREATED)
