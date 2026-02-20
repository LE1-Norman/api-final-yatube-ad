from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class ConditionalLimitOffsetPagination(LimitOffsetPagination):
    """Пагинация при использовании параметров limit/offset"""

    def paginate_queryset(self, queryset, request, view=None):
        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        if not limit and not offset:
            return None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        if self.count is None:
            return Response(data)
        return super().get_paginated_response(data)
