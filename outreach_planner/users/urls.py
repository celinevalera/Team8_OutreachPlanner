from django.urls import path
from . import views 

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('profile',views.view_profile, name="view_profile"),
    path('edit_profile', views.edit_profile, name='edit-profile'),
    path('change-password', views.change_password, name='change_password')
]
