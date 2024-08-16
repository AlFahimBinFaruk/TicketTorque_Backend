import uuid
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from ..models import Order
from ticket.models import Ticket
from account.models import Account
from datetime import datetime
from core.ValidateUser import IsAuthenticatedMixin

class Controller(IsAuthenticatedMixin, APIView):
    def post(self, request, *args, **kwargs):
        jwt_payload = getattr(request, 'jwt_payload', None)

        user_id=jwt_payload.get("id")
        
        data = request.data

        ticket_id = data.get('ticket_id')
        qty = data.get('qty')
        

        # Basic validation
        if not ticket_id or not user_id or not qty:
            return JsonResponse({'error': 'All required fields must be provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            ticket = Ticket.objects.get(id=ticket_id)
            user = Account.objects.get(id=user_id)
        except Ticket.DoesNotExist:
            return JsonResponse({'error': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND)
        except Account.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Create order
        order = Order(
            id=uuid.uuid4(),  # Generate a new UUID
            ticket=ticket,
            user=user,
            qty=qty,
            payment_date=None,
            payment_status="pending",
            order_status="pending",
            transaction_id=None,
        )
        order.save()

        return JsonResponse({'message': 'Order created successfully', 'order_id': str(order.id)}, status=status.HTTP_201_CREATED)
