from django.urls import path
from .views import register_user, user_login,user_logout

urlpatterns = [
    path('register/', register_user.as_view(), name='register'),
    path('login/', user_login.as_view(), name='login'),
    path('logout/', user_logout.as_view(), name='logout'),
]