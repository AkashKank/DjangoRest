# from rest_framework.pagination import CursorPagination
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
    ordering = 'published_date'


# class MyCursorPagination(CursorPagination):
#     page_size = 5
#     # ordering = 'id'
#     ordering = 'name'