from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from ..models import Order
from core.ValidateAdmin import AdminRoleMixin

class Controller(AdminRoleMixin, APIView):
    def post(self, request, *args, **kwargs):
        
        data = request.data
        order_id = data.get('order_id')
        order_status = data.get('order_status')
        payment_status = data.get('payment_status')

        # Basic validation
        if not order_id or not order_status or not payment_status:
            return JsonResponse({'error': 'Order ID and order and payment status must be provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(id=order_id)

            

            # update
            order.order_status=order_status
            order.payment_status=payment_status
            order.save()

            return JsonResponse({'message': 'Order status successfully'}, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
