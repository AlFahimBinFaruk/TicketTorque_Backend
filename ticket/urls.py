from django.urls import path

from .controllers import AddNewTicketController,DeleteTicketController,UpdateTicketController,GetTicketListController, GetTicketDetailsController

urlpatterns=[
    path("ticket/add-new",AddNewTicketController.Controller.as_view(),name="add-new-ticket-view"),
    path("ticket/update/<uuid:ticket_id>",UpdateTicketController.Controller.as_view(),name="update-ticket-view"),
    path("ticket/delete/<uuid:ticket_id>",DeleteTicketController.Controller.as_view(),name="delete-ticket-view"),
    path("ticket/details/<uuid:ticket_id>",GetTicketDetailsController.Controller.as_view(),name="get-ticket-details-view"),
    path("ticket/all",GetTicketListController.Controller.as_view(),name="get-ticket-list-view"),


]