from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from ..models import Vehicle
from core.ValidateAdmin import AdminRoleMixin



class Controller(AdminRoleMixin, APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Extract vehicle name from request data
            name = request.data.get('name')

            if not name:
                return JsonResponse({'error': 'Name is required.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create and save the new vehicle
            vehicle = Vehicle.objects.create(name=name)

            return Response({
                'id': str(vehicle.id),
                'name': vehicle.name,
                'created_at': vehicle.created_at,
                'updated_at': vehicle.updated_at
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
