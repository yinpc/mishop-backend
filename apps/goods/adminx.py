import xadmin
from .models import Goods, GoodsCategory, GoodsImage, Banner


class GoodsAdmin(object):
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "shop_price",
                    "shop_old_price", "goods_brief", "goods_desc", "goods_red_label", "is_new", "is_hot", "add_time"]
    search_fields = ['name', ]
    list_editable = ["is_hot", ]
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "shop_price",
                   "is_new", "is_hot", "add_time", "category__name"]
    # style_fields = {"goods_desc": "ueditor"}

    class GoodsImagesInline(object):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'accordion'

    inlines = [GoodsImagesInline]


class GoodsCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


class BannerGoodsAdmin(object):
    list_display = ["goods", "image", "index"]


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Banner, BannerGoodsAdmin)
