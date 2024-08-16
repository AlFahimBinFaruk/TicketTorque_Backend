from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from uuid import UUID
from ..models import Account
from core.ValidateAdmin import AdminRoleMixin


class Controller(AdminRoleMixin,APIView):
    def delete(self, request, user_id, *args, **kwargs):
        try:
            # Validate that the user_id is a valid UUID
            try:
                uuid_obj = UUID(str(user_id), version=4)
            except ValueError:
                return JsonResponse({'error': 'Invalid user ID format.'}, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve the user object by id or return 404 if not found
            user = get_object_or_404(Account, id=uuid_obj)

            # Delete the user
            user.delete()

            # Return a success response
            return Response({'message': 'User profile deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

        except Account.DoesNotExist:
            # If the user with the given id does not exist
            return JsonResponse({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Generic catch-all for any other exceptions
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
