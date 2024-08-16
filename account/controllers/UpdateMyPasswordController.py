from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
from uuid import UUID
from ..models import Account
from core.ValidateUser import IsAuthenticatedMixin


class Controller(IsAuthenticatedMixin, APIView):
    def put(self, request, *args, **kwargs):
        try:
            jwt_payload = getattr(request, 'jwt_payload', None)

            user_id=jwt_payload.get("id")
            # Validate that the user_id is a valid UUID
            try:
                uuid_obj = UUID(str(user_id), version=4)
            except ValueError:
                return JsonResponse({'error': 'Invalid user ID format.'}, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve the user object by id or return 404 if not found
            user = get_object_or_404(Account, id=uuid_obj)

            # Get the current and new password from the request data
            cur_password = request.data.get('cur_password')
            new_password = request.data.get('new_password')

            if not cur_password or not new_password:
                return JsonResponse({'error': 'Current and new passwords are required.'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the current password is correct
            if not check_password(cur_password, user.password):
                return JsonResponse({'error': 'Current password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

            # Update the user's password
            user.password = make_password(new_password)
            user.save()

            # Return a success response
            return Response({'message': 'Password updated successfully.'}, status=status.HTTP_200_OK)

        except Account.DoesNotExist:
            # If the user with the given id does not exist
            return JsonResponse({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Generic catch-all for any other exceptions
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
