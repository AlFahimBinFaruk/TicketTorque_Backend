import jwt
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.mixins import AccessMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class IsAuthenticatedMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        token = request.headers.get('Authorization', None)
        if token is None:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        try:
            # Remove "Bearer " if it exists
            if token.startswith('Bearer '):
                token = token[7:]

            # Decode the token
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            
            
            
            # Set the decoded token to a custom attribute
            request.jwt_payload = decoded_token

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        return super().dispatch(request, *args, **kwargs)
