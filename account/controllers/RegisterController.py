import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from ..models import Account
from datetime import datetime, timedelta


class Controller(APIView):
    def post(self, request, *args, **kwargs):
        # Get user data from request
        data = request.data
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name', '')
        phone = data.get('phone', '')
        

        # Basic validation
        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if Account.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        # Create user
        user = Account(
            email=email,
            password=make_password(password),  # Hash the password
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role="user"
        )
        user.save()

        # Generate JWT token
        payload = {
            'id': str(user.id),
            'email': user.email,
            'role':user.role,
            'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiration
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return JsonResponse({'token': token}, status=status.HTTP_201_CREATED)
