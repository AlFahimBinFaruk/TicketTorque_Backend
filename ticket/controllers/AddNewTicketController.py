import uuid
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from ..models import Ticket
from vehicle.models import Vehicle
from category.models import Category
from location.models import Location
from datetime import datetime
from core.ValidateAdmin import AdminRoleMixin

class Controller(AdminRoleMixin,APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        # Extract data from request
        name = data.get('name')
        vehicle_id = data.get('vehicle_id')
        category_id = data.get('category_id')
        price = data.get('price')
        qty = data.get('qty')
        arrival_date = data.get('arrival_date')
        departure_date = data.get('departure_date')
        boarding_point_name = data.get('boarding_point_name')
        dropping_point_name = data.get('dropping_point_name')
        from_location_id = data.get('from_location_id')
        to_location_id = data.get('to_location_id')

        # Validate required fields
        if not all([name, vehicle_id, category_id, price, qty, arrival_date, departure_date, boarding_point_name, dropping_point_name, from_location_id, to_location_id]):
            return JsonResponse({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

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
            arrival_date = datetime.strptime(arrival_date, '%Y-%m-%d').date()
            departure_date = datetime.strptime(departure_date, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save Ticket
        try:
            ticket = Ticket(
                id=uuid.uuid4(),
                name=name,
                vehicle=vehicle,
                category=category,
                price=price,
                qty=qty,
                arrival_date=arrival_date,
                departure_date=departure_date,
                boarding_point_name=boarding_point_name,
                dropping_point_name=dropping_point_name,
                from_location=from_location,
                to_location=to_location
            )
            ticket.save()
        except Exception as e:
            return JsonResponse({'error': f'An error occurred while saving the ticket: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse({'message': 'Ticket created successfully', 'ticket_id': str(ticket.id)}, status=status.HTTP_201_CREATED)
