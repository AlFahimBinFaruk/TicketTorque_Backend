from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from ..models import Order
from core.ValidateUser import IsAuthenticatedMixin
from datetime import datetime


class Controller(IsAuthenticatedMixin, APIView):
    def post(self, request, *args, **kwargs):
        jwt_payload = getattr(request, 'jwt_payload', None)

        user_id = jwt_payload.get("id")
        data = request.data
        order_id = data.get('order_id')
        transaction_id = data.get('transaction_id')

        # Basic validation
        if not order_id or not transaction_id:
            return JsonResponse({'error': 'Order ID and transaction ID must be provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(id=order_id)

            # Check if the order belongs to the current user
            if str(order.user.id) != user_id:
                return JsonResponse({'error': 'Unauthorized to update this order'}, status=status.HTTP_403_FORBIDDEN)

            # Add the transaction ID to the order
            order.transaction_id = transaction_id
            order.payment_date=datetime.now()
            order.save()

            return JsonResponse({'message': 'Transaction ID added successfully'}, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
