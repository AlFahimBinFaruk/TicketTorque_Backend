from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Category

class Controller(APIView):
    def get(self, request, category_id, *args, **kwargs):
        try:
            # Retrieve the category by id or return 404 if not found
            category = get_object_or_404(Category, id=category_id)

            # Return the category details
            return Response({
                'id': str(category.id),
                'name': category.name,
                'created_at': category.created_at,
                'updated_at': category.updated_at
            }, status=status.HTTP_200_OK)

        except Category.DoesNotExist:
            # This should not be reached because get_object_or_404 would handle it
            return JsonResponse({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Generic catch-all for any other exceptions
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
