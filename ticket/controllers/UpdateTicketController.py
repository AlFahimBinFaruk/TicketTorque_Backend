import uuid
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from ..models import Ticket
from vehicle.models import Vehicle
from category.models import Category
from location.models import Location
from datetime import datetime
from core.ValidateAdmin import AdminRoleMixin

class Controller(AdminRoleMixin, APIView):
    def put(self, request,ticket_id , *args, **kwargs):
        data = request.data

        # Validate ticket ID
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return JsonResponse({'error': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND)

        # Extract data from request
        name = data.get('name', ticket.name)
        vehicle_id = data.get('vehicle_id', ticket.vehicle.id)
        category_id = data.get('category_id', ticket.category.id)
        price = data.get('price', ticket.price)
        qty = data.get('qty', ticket.qty)
        arrival_date = data.get('arrival_date', ticket.arrival_date)
        departure_date = data.get('departure_date', ticket.departure_date)
        boarding_point_name = data.get('boarding_point_name', ticket.boarding_point_name)
        dropping_point_name = data.get('dropping_point_name', ticket.dropping_point_name)
        from_location_id = data.get('from_location_id', ticket.from_location.id)
        to_location_id = data.get('to_location_id', ticket.to_location.id)

        # Validate and process foreign keys
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id)
        except Vehicle.DoesNotExist:
            return JsonResponse({'error': 'Invalid vehicle ID'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Invalid category ID'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            from_location = Location.objects.get(id=from_location_id)
        except Location.DoesNotExist:
            return JsonResponse({'error': 'Invalid from location ID'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            to_location = Location.objects.get(id=to_location_id)
        except Location.DoesNotExist:
            return JsonResponse({'error': 'Invalid to location ID'}, status=status.HTTP_400_BAD_REQUEST)

        # Parse and validate dates
        try:
            if arrival_date:
                arrival_date = datetime.strptime(arrival_date, '%Y-%m-%d').date()
            if departure_date:
                departure_date = datetime.strptime(departure_date, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        # Update and save Ticket
        try:
            ticket.name = name
            ticket.vehicle = vehicle
            ticket.category = category
            ticket.price = price
            ticket.qty = qty
            ticket.arrival_date = arrival_date
            ticket.departure_date = departure_date
            ticket.boarding_point_name = boarding_point_name
            ticket.dropping_point_name = dropping_point_name
            ticket.from_location = from_location
            ticket.to_location = to_location
            ticket.save()
        except Exception as e:
            return JsonResponse({'error': f'An error occurred while updating the ticket: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse({'message': 'Ticket updated successfully'}, status=status.HTTP_200_OK)
