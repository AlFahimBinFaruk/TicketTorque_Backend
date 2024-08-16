from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from ..models import Account
from ..serializers import AccountSerializer
from core.ValidateAdmin import AdminRoleMixin


class Controller(AdminRoleMixin,APIView):
    def get(self, request, *args, **kwargs):
        # Query all users
        users = Account.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(users, request)
        
        # Serialize data
        serializer = AccountSerializer(page, many=True)
        
        # Return paginated response
        return paginator.get_paginated_response(serializer.data)
