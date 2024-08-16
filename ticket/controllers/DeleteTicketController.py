from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from ..models import Ticket

from core.ValidateAdmin import AdminRoleMixin

class Controller(AdminRoleMixin,APIView):
    def delete(self, request,ticket_id, *args, **kwargs):

        # Validate ticket ID
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return JsonResponse({'error': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND)

        # Delete ticket
        try:
            ticket.delete()
        except Exception as e:
            return JsonResponse({'error': f'An error occurred while deleting the ticket: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse({'message': 'Ticket deleted successfully'}, status=status.HTTP_200_OK)
