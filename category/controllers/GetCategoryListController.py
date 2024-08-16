from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from ..models import Category

class Controller(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Retrieve all categories from the database
            categories = Category.objects.all().values('id', 'name')

            # Return the list of categories
            return Response({
                'categories': list(categories)
            }, status=status.HTTP_200_OK)

        except Exception as e:
            # Generic catch-all for any other exceptions
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
