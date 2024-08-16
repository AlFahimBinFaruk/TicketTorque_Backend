from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from ..models import Order
from core.ValidateAdmin import AdminRoleMixin

class Controller(AdminRoleMixin, APIView):
    def get(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Set the page size

        try:
            orders = Order.objects.all().order_by('-created_at')  # Get all orders, sorted by creation date
            result_page = paginator.paginate_queryset(orders, request)
            
            orders_list = [{
                'id': str(order.id),
                'payment_status': order.payment_status
            } for order in result_page]

            return paginator.get_paginated_response(orders_list)

        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
