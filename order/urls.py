from django.urls import path

from .controllers import (
    AddNewOrderController,
    CancelMyOrderController,
    GetMyOrderDetailsController,
    GetOrderDetailsController,
    GetMyOrderListController,
    GetOrderListController,
    HandleOrderStatusController,
    UpdateTransactionIdController
)

urlpatterns=[
    path("order/add-new",AddNewOrderController.Controller.as_view(),name="add-new-order-view"),

    path("order/update/tran-id",UpdateTransactionIdController.Controller.as_view(),name="update-tran-id-view"),
    
    path("order/all",GetOrderListController.Controller.as_view(),name="get-order-list-view"),

    path("order/my/all",GetMyOrderListController.Controller.as_view(),name="get-my-order-list-view"),
    
    path("order/details/<uuid:order_id>",GetOrderDetailsController.Controller.as_view(),name="get-order-details-view"),

    path("order/my/details/<uuid:order_id>",GetMyOrderDetailsController.Controller.as_view(),name="get-my-order-details-view"),
    
    path("order/my/cancel",CancelMyOrderController.Controller.as_view(),name="cancel-my-order-view"),
    
    
    
    path("order/update",HandleOrderStatusController.Controller.as_view(),name="handle-order-status-view"),
    
    


]