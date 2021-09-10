import xadmin
from .models import UserProfile

class UserProfileAdminx(object):
    """用户信息管理后台"""
    list_display = ['']
    list_filter = ['']
    search_fields = ['']


xadmin.site.register(UserProfile, UserProfileAdminx)