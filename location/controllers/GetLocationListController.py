from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from ..models import Location

class Controller(APIView):
    def get(self, request, *args, **kwargs):
        try:
            locations = Location.objects.all().values('id', 'name')
            return Response({
                'locations': list(locations)
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
