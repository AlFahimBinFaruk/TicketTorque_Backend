from django.urls import path

from .controllers import AddNewLocationController,DeleteLocationController,GetLocationDetailsController,GetLocationListController,UpdateLocationController

urlpatterns=[
        path("location/add-new",AddNewLocationController.Controller.as_view(),name="add-new-location-view"),
        path("location/update/<uuid:location_id>",UpdateLocationController.Controller.as_view(),name="update-location-view"),
        path("location/delete/<uuid:location_id>",DeleteLocationController.Controller.as_view(),name="delete-location-view"),
        path("location/details/<uuid:location_id>",GetLocationDetailsController.Controller.as_view(),name="get-location-details-view"),
        path("location/all",GetLocationListController.Controller.as_view(),name="get-location-list-view"),

]