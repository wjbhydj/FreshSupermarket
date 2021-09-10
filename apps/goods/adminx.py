import xadmin
from .models import Goods, GoodsCategory, GoodsImage, Banner, HotSearchWords, GoodsCategoryBrand, IndexAd

class GoodsAdminx(object):
    """商品管理后台"""
    list_display = ['name','goods_sn','category','click_num','sold_num','fav_num','goods_num','market_price',
                    'shop_price','goods_brief','goods_desc','ship_free','goods_front_image','is_new','is_hot','add_time']
    search_fields = ['name',]
    list_editable = ['is_hot',]
    list_filter = ['name','goods_sn','category','click_num','sold_num','fav_num','goods_num','market_price',
                    'shop_price','ship_free','goods_front_image','is_new','is_hot','add_time', 'category__name']
    style_fields = {'goods_desc':'ueditor'}

    class GoodsImageInline(object):
        model = GoodsImage
        exclude = 'add_time'
        extra = 1
        style = 'tab'

    inlines = [GoodsImageInline,]


class GoodsCategoryAdminx(object):
    """商品分类管理后台"""
    list_display = ['name','category_type','parent_category','add_time']
    list_filter = ['name','category_type','parent_category']
    search_fields = ['name',]


class GoodsCategoryBrandAdminx(object):
    """商品广告"""
    list_display = ['category', 'name', 'desc', 'image', 'add_time']

    def get_context(self):
        context = super(GoodsCategoryBrandAdminx, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
        return context


class BannerAdminx(object):
    """首页轮播的商品管理后台"""
    list_display = ['goods', 'image', 'index', 'add_time']


class HotsearchWordsAdminx(object):
    """搜索栏下方热搜词管理后台"""
    list_display = ['keywords', 'index', 'add_time']


class IndexAdAadminx(object):
    """商品广告管理后台"""
    list_display = ['category', 'goods']


xadmin.site.register(Goods, GoodsAdminx)
xadmin.site.register(GoodsCategory, GoodsCategoryAdminx)
xadmin.site.register(GoodsCategoryBrand, GoodsCategoryBrandAdminx)
xadmin.site.register(Banner, BannerAdminx)
xadmin.site.register(HotSearchWords, HotsearchWordsAdminx)
xadmin.site.register(IndexAd, IndexAdAadminx)