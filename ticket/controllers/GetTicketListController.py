from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from ..models import Ticket

class Controller(APIView):
    def get(self, request, *args, **kwargs):
        # Extract query parameters
        category_id = request.query_params.get('category_id', None)
        vehicle_id = request.query_params.get('vehicle_id', None)
        from_location_id = request.query_params.get('from', None)
        to_location_id = request.query_params.get('to', None)

        # Filter tickets based on query parameters
        filters = {}
        if category_id:
            filters['category_id'] = category_id
        if vehicle_id:
            filters['vehicle_id'] = vehicle_id
        if from_location_id:
            filters['from_location_id'] = from_location_id
        if to_location_id:
            filters['to_location_id'] = to_location_id

        tickets = Ticket.objects.filter(**filters)

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Set the number of items per page
        paginated_tickets = paginator.paginate_queryset(tickets, request)

        # Prepare response data
        ticket_data = [{
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
        } for ticket in paginated_tickets]

        # Return paginated response
        return paginator.get_paginated_response(ticket_data)
