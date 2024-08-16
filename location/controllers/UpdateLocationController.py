from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Location
from core.ValidateAdmin import AdminRoleMixin

class Controller(AdminRoleMixin, APIView):
    def put(self, request, location_id, *args, **kwargs):
        try:
            location = get_object_or_404(Location, id=location_id)
            name = request.data.get('name')

            if name is not None:
                location.name = name

            location.save()
            return Response({
                'msg': 'location updated successfully'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
