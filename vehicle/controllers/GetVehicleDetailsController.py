from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Vehicle

class Controller(APIView):
    def get(self, request, vehicle_id, *args, **kwargs):
        try:
            # Retrieve the vehicle by id or return 404 if not found
            vehicle = get_object_or_404(Vehicle, id=vehicle_id)

            return Response({
                'id': str(vehicle.id),
                'name': vehicle.name,
                'created_at': vehicle.created_at,
                'updated_at': vehicle.updated_at
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
