import xadmin
from .models import UserFav, UserAddress, UserLeavingMessage

class UserFavAdminx(object):
    """收藏管理"""
    list_display = ['user', 'goods', 'add_time']


class UserAddressAdminx(object):
    """用户地址管理"""
    list_display = ['user', 'province', 'city', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time']


class UserLeavingMessageAdminx(object):
    """用户留言管理"""
    list_display = ['user', 'message_type', 'message', 'add_time']


xadmin.site.register(UserFav, UserFavAdminx)
xadmin.site.register(UserAddress, UserAddressAdminx)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdminx)