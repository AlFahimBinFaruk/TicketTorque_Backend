import jwt
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime, timedelta
from ..models import Account

class Controller(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        # Basic validation
        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch the user by email
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Check password
        if not check_password(password, user.password):
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT token
        payload = {
            'id': str(user.id),
            'email': user.email,
            'role':user.role,
            'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiration
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return JsonResponse({'token': token}, status=status.HTTP_200_OK)
