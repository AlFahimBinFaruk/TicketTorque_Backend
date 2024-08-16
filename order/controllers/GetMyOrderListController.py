from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from ..models import Order
from core.ValidateUser import IsAuthenticatedMixin

class Controller(IsAuthenticatedMixin, APIView):
    def get(self, request, *args, **kwargs):
        jwt_payload = getattr(request, 'jwt_payload', None)
        user_id = jwt_payload.get("id")

        # Get the page number from the request
        page_number = request.GET.get('page', 1)
        page_size = 10  # You can adjust the page size as needed

        try:
            # Filter orders by the current user
            orders = Order.objects.filter(user__id=user_id).order_by('-created_at')

            # Paginate the orders
            paginator = Paginator(orders, page_size)
            page_obj = paginator.get_page(page_number)

            # Serialize the order data
            orders_list = []
            for order in page_obj:
                orders_list.append({
                    'id': str(order.id),
                    'payment_status': order.payment_status,
                })

            response_data = {
                'count': paginator.count,
                'num_pages': paginator.num_pages,
                'current_page': page_obj.number,
                'next_page': page_obj.next_page_number() if page_obj.has_next() else None,
                'previous_page': page_obj.previous_page_number() if page_obj.has_previous() else None,
                'orders': orders_list,
            }

            return JsonResponse(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
