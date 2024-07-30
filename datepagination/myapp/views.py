from django.shortcuts import render
from .models import Profile
from rest_framework.generics import ListAPIView
from .serializer import PaginationSerializers
from .mypagination import CustomPagination
from rest_framework import generics
from django.utils.dateparse import parse_date
from django.utils import timezone

# Create your views here.
# class PaginationAPIView(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = PaginationSerializers
#     pagination_class = DateRangePagination


class EventListView(generics.ListAPIView):
    serializer_class = PaginationSerializers
    pagination_class = CustomPagination  # If using a custom paginator

    def get_queryset(self):
        queryset = Profile.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if start_date:
            queryset = queryset.filter(published_date__gte=parse_date(start_date))

        if end_date:
            queryset = queryset.filter(published_date__lte=parse_date(end_date))

        return queryset