from django.urls import path
from .views import ImportAPIView, PaginationAPIView

urlpatterns = [
    path("appview/",ImportAPIView.as_view(), name="appview"),
    path("paginationview/",PaginationAPIView.as_view(), name="appview")
]