from django.urls import path

from .controllers import RegisterController, LoginController, GetUserListController, GetUserDetailsController,GetMyProfileDetailsController, DeleteUserProfileController, UpdateUserProfileController, UpdateMyProfileController , UpdateMyPasswordController

urlpatterns=[
    path("user/register",RegisterController.Controller.as_view(),name="register-view"),

    path("user/login",LoginController.Controller.as_view(),name="login-view"),
    
    path("user/all",GetUserListController.Controller.as_view(),name="get-user-list-view"),
    
    path("user/details/<uuid:user_id>",GetUserDetailsController.Controller.as_view(),name="get-user-details-view"),
    
    path("user/details/my-profile",GetMyProfileDetailsController.Controller.as_view(),name="get-my-profile-details-view"),
    
    path("user/delete/<uuid:user_id>",DeleteUserProfileController.Controller.as_view(),name="delete-user-profile-view"),
    
    path("user/update/<uuid:user_id>",UpdateUserProfileController.Controller.as_view(),name="update-user-profile-view"),
    
    path("user/update/my-profile",UpdateMyProfileController.Controller.as_view(),name="update-my-profile-view"),
    
    path("user/update/my-password",UpdateMyPasswordController.Controller.as_view(),name="update-my-password-view"),


]