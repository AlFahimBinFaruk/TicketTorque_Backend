from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Category
from core.ValidateAdmin import AdminRoleMixin

class Controller(AdminRoleMixin, APIView):
    def put(self, request, category_id, *args, **kwargs):
        try:
            # Retrieve the category by id or return 404 if not found
            category = get_object_or_404(Category, id=category_id)

            # Get the updated name from the request data
            new_name = request.data.get('name')

            if not new_name:
                return JsonResponse({'error': 'Category name is required.'}, status=status.HTTP_400_BAD_REQUEST)

            # Update the category's name
            category.name = new_name
            category.save()

            # Return a success response
            return Response({
                'message': 'category updated successfully'
            }, status=status.HTTP_200_OK)

        except Category.DoesNotExist:
            # If the category with the given id does not exist
            return JsonResponse({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Generic catch-all for any other exceptions
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
