from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from ..models import Location
from core.ValidateAdmin import AdminRoleMixin


class Controller(AdminRoleMixin, APIView):
    def post(self, request, *args, **kwargs):
        try:
            name = request.data.get('name')
            if not name:
                return JsonResponse({'error': 'Name is required.'}, status=status.HTTP_400_BAD_REQUEST)

            location = Location.objects.create(name=name)
            return Response({
                'id': str(location.id),
                'name': location.name,
                'created_at': location.created_at,
                'updated_at': location.updated_at
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
