from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from ..models import Category
from core.ValidateAdmin import AdminRoleMixin

class Controller(AdminRoleMixin, APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Get the category name from the request data
            name = request.data.get('name')

            if not name:
                return JsonResponse({'error': 'Category name is required.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new category
            category = Category(name=name)
            category.save()

            # Return a success response
            return Response({
                'id': str(category.id),
                'name': category.name,
                'created_at': category.created_at,
                'updated_at': category.updated_at
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Generic catch-all for any other exceptions
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
