from django.urls import path
from .views import *

urlpatterns = [
    # path("countryview/",MedalCountListCreateView.as_view(),name="countryview"),
    path("medalview/",MedalCountListView.as_view(),name="medalview"),
]