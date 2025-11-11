from  rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 5       # show 5 items per page
    page_size_query_param = 'page_size'  # user can change with ?page_size=10
    max_page_size = 50