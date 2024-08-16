from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from uuid import UUID
from ..models import Account
from core.ValidateUser import IsAuthenticatedMixin


class Controller(IsAuthenticatedMixin,APIView):
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

            # Get the data from the request
            data = request.data

            # Manually update each field if it's provided in the request data
            if 'first_name' in data:
                user.first_name = data['first_name']
            if 'last_name' in data:
                user.last_name = data.get('last_name', '')  # Default to an empty string if not provided
            if 'email' in data:
                user.email = data['email']
            if 'phone' in data:
                user.phone = data.get('phone', '')  # Default to an empty string if not provided
            if 'role' in data:
                user.role = data['role']

            # Update the `updated_at` timestamp
            user.save()

            # Return a success response
            return Response({
                'message': 'User profile updated successfully.'
            }, status=status.HTTP_200_OK)

        except Account.DoesNotExist:
            # If the user with the given id does not exist
            return JsonResponse({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Generic catch-all for any other exceptions
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
