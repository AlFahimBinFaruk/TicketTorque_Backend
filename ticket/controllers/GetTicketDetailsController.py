from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from ..models import Ticket

class Controller(APIView):
    def get(self, request, ticket_id, *args, **kwargs):
       

        # Validate ticket ID
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return JsonResponse({'error': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND)

        # Prepare ticket data for response
        ticket_data = {
            'id': str(ticket.id),
            'name': ticket.name,
            'vehicle': {
                'id': str(ticket.vehicle.id),
                'name': ticket.vehicle.name
            },
            'category': {
                'id': str(ticket.category.id),
                'name': ticket.category.name
            },
            'price': ticket.price,
            'qty': ticket.qty,
            'arrival_date': ticket.arrival_date,
            'departure_date': ticket.departure_date,
            'boarding_point_name': ticket.boarding_point_name,
            'dropping_point_name': ticket.dropping_point_name,
            'from_location': {
                'id': str(ticket.from_location.id),
                'name': ticket.from_location.name
            },
            'to_location': {
                'id': str(ticket.to_location.id),
                'name': ticket.to_location.name
            },
            'created_at': ticket.created_at,
            'updated_at': ticket.updated_at
        }

        return JsonResponse(ticket_data, status=status.HTTP_200_OK)
