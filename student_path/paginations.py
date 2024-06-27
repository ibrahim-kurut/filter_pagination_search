from rest_framework.pagination import PageNumberPagination

class Custom_Pagination_Student(PageNumberPagination):
    page_size = 50
    page_query_param = 'page'


class Custom_Pagination_Path(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'