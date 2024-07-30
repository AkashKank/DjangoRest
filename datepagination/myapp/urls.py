from django.urls import path
from .views import EventListView

urlpatterns = [
    path("paginationview/",EventListView.as_view(), name="appview"),
]