from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from ..models import Vehicle

class Controller(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Retrieve all vehicles with only necessary fields
            vehicles = Vehicle.objects.all().values('id', 'name')

            return Response({
                'vehicles': list(vehicles)
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)