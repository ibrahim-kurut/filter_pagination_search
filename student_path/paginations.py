from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class Custom_Pagination_Student(PageNumberPagination):
    page_size = 50
    page_query_param = 'page'


class Custom_Pagination_Path(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'



class Custom_Limit_Offset_Student(LimitOffsetPagination):
     default_limit = 10
     limit_query_param = 'limit'
     offset_query_param = 'offset'


class Custom_Limit_Offset_Path(LimitOffsetPagination):
     default_limit = 2
     limit_query_param = 'limit'
     offset_query_param = 'offset'

class Custom_Cursor_Pagination(CursorPagination):
    page_size = 20
    cursor_query_param = "cursor"















