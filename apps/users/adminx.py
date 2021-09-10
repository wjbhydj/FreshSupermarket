import xadmin
from xadmin import views
from .models import UserProfile, VerifyCode

class BaseSetting(object):
    """添加主题"""
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    """全局配置"""
    site_title = '银信达'
    site_footer = "http://www.cnblogs.com/derek1184405959/"
    menu_style = 'accordion'    #菜单收缩


class UserProfileAdminx(object):
    """用户信息管理后台"""
    list_display = ['username', 'password', 'name', 'gender', 'mobile', 'email', 'birthday']
    list_filter = ['username', 'password', 'name', 'gender', 'mobile', 'email', 'birthday']
    search_fields = ['username', 'password', 'name', 'gender', 'mobile', 'email', 'birthday']


class VerifyCodeAdminx(object):
    """验证码管理后台"""
    list_display = ['code', 'mobile', 'add_time']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
# xadmin.site.register(UserProfile, UserProfileAdminx)
xadmin.site.register(VerifyCode, VerifyCodeAdminx)