import xadmin
from xadmin import views
from .models import UserProfile


# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True

class UserProfileAdmin(object):
    list_display = ["name", "portrait", "openid", "add_time"]
    # list_display_links = ("name",)


class GlobalSettings(object):
    site_title = "米铺"
    site_footer = "mishop"
    # menu_style = "accordion"


# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
