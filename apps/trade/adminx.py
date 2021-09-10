import xadmin
from .models import OrderInfo, OrderGoods, ShoppingCart

class ShoppingCartAdminx(object):
    """购物车管理后台"""
    list_display = ['user', 'goods', 'nums']


class OrderInfoAdminx(object):
    """订单信息管理"""
    list_display = ['user','order_sn','trade_no','pay_status','post_script',
                    'order_mount','pay_time','add_time']

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time',]
        extra = 1
        style = 'tab'
    inlines = [OrderGoodsInline,]


xadmin.site.register(ShoppingCart, ShoppingCartAdminx)
xadmin.site.register(OrderInfo, OrderInfoAdminx)