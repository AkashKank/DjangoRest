from django.urls import path
from .views import register_user, new_user_register, new_user_login

urlpatterns = [
    path('register/', register_user.as_view(), name='register'),
    path('newregister/', new_user_register.as_view(), name='newregister'),
    path('newuserlogin/', new_user_login.as_view(), name='newuserlogin'),
]