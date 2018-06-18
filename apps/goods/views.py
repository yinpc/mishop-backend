from .serializers import CategorySerializer, GoodsSerializer
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import GoodsCategory, Goods
from rest_framework import viewsets


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class CategoryListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('category_type',)
    search_fields = ('name',)
    # pagination_class = Pagination

# def post(self, request):
#     serializer = GoodsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品列表页, 分页， 搜索， 过滤， 排序
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = Pagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.click_num += 1
    #     instance.save()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
