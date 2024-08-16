from django.urls import path

from .controllers import AddNewVehicleController,DeleteVehicleController,GetVehicleDetailsController,GetVehicleListController,UpdateVehicleController

urlpatterns=[
        path("vehicle/add-new",AddNewVehicleController.Controller.as_view(),name="add-new-vehicle-view"),
        path("vehicle/update/<uuid:vehicle_id>",UpdateVehicleController.Controller.as_view(),name="update-vehicle-view"),
        path("vehicle/delete/<uuid:vehicle_id>",DeleteVehicleController.Controller.as_view(),name="delete-vehicle-view"),
        path("vehicle/details/<uuid:vehicle_id>",GetVehicleDetailsController.Controller.as_view(),name="get-vehicle-details-view"),
        path("vehicle/all",GetVehicleListController.Controller.as_view(),name="get-vehicle-list-view"),

]