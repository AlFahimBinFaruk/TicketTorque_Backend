from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Vehicle
from core.ValidateAdmin import AdminRoleMixin


class Controller(AdminRoleMixin, APIView):
    def put(self, request, vehicle_id, *args, **kwargs):
        try:
            # Retrieve the vehicle by id or return 404 if not found
            vehicle = get_object_or_404(Vehicle, id=vehicle_id)

            # Extract fields to update from request data
            name = request.data.get('name')

            if name is not None:
                vehicle.name = name
            
            # Save the updated vehicle
            vehicle.save()

            return Response({
                'msg': 'vehicle updated successfully'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
