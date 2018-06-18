"""mishop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from goods.views import CategoryListViewSet, GoodsListViewSet
from rest_framework.routers import DefaultRouter
from django.views.static import serve
from mishop.settings import MEDIA_ROOT

xadmin.autodiscover()

from xadmin.plugins import xversion

xversion.register_models()

router = DefaultRouter()
router.register('category', CategoryListViewSet)
router.register(r'goods', GoodsListViewSet, base_name="goods")

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    path('docs/', include_docs_urls(title='mishop'))
]

'''
yinp
admin123
'''
