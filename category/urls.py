from django.urls import path

from .controllers import AddNewCategoryController,DeleteCategoryController,UpdateCategoryController,GetCategoryListController, GetCategoryDetailsController

urlpatterns=[
    path("category/add-new",AddNewCategoryController.Controller.as_view(),name="add-new-category-view"),
    path("category/update/<uuid:category_id>",UpdateCategoryController.Controller.as_view(),name="update-category-view"),
    path("category/delete/<uuid:category_id>",DeleteCategoryController.Controller.as_view(),name="delete-category-view"),
    path("category/details/<uuid:category_id>",GetCategoryDetailsController.Controller.as_view(),name="get-category-details-view"),
    path("category/all",GetCategoryListController.Controller.as_view(),name="get-category-list-view"),


]