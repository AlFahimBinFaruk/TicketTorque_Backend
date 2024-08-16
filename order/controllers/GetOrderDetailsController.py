from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from ..models import Order
from core.ValidateAdmin import AdminRoleMixin

class Controller(AdminRoleMixin, APIView):
    def get(self, request, order_id, *args, **kwargs):
        

        try:
            order = Order.objects.get(id=order_id)

            
            # Prepare order details excluding ticket's created_at and updated_at
            order_details = {
                'id': str(order.id),
                'ticket': {
                    'id': str(order.ticket.id),
                    'name': order.ticket.name,
                    'price': order.ticket.price,
                    'vehicle': {
                        'id': str(order.ticket.vehicle.id),
                        'name': order.ticket.vehicle.name,
                    },
                    'category': {
                        'id': str(order.ticket.category.id),
                        'name': order.ticket.category.name,
                    },
                    'from_location': {
                        'id': str(order.ticket.from_location.id),
                        'name': order.ticket.from_location.name,
                    },
                    'to_location': {
                        'id': str(order.ticket.to_location.id),
                        'name': order.ticket.to_location.name,
                    },
                    'arrival_date': order.ticket.arrival_date,
                    'departure_date': order.ticket.departure_date,
                    'boarding_point_name': order.ticket.boarding_point_name,
                    'dropping_point_name': order.ticket.dropping_point_name,
                },
                'user': {
                    'id': str(order.user.id),
                    'email': order.user.email,
                },
                'qty': order.qty,
                'payment_date': order.payment_date,
                'payment_status': order.payment_status,
                'transaction_id': order.transaction_id,
                'created_at': order.created_at,
                'updated_at': order.updated_at
            }

            return JsonResponse(order_details, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
