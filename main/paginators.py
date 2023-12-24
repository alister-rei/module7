from rest_framework.pagination import PageNumberPagination


class CoursePaginator(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 20


class LessonPaginator(PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 20


class UserPaginator(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 20
