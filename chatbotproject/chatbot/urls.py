from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('conversationtopic/', ConversationTopicListCreateView.as_view(), name='conversationtopic'),
    path('messagecreate/', MessageCreateView.as_view(), name='messagecreate'),
]
