# @Time    : 18-10-31
# @Author  : Zhiqi Kou
# @Email   : zhiqi1028@gmail.com

from django.urls import path, re_path,include
from .views import *

urlpatterns = [
    # 游记点赞
    path('fav/', FavView.as_view(), name='fav'),
    # 游记收藏
    path('collect/', CollView.as_view(), name='collect'),
    # 游记评论
    path('comments/', CommentsView.as_view(), name='comments'),

    # 购物车
    path('shopcar/', ShopcarView.as_view(), name='shopcar'),
    # 购物车操作,操作：add(数量加1)/reduce(数量减1)/checked(商品选中)/uncheck(商品不选中)/正整数(直接修改数量)
    path('shopcaroperation/', ShopcarOperationView.as_view(), name='shopcaroperation'),
    # 直接购买商品
    path('shoping/', ShopingView.as_view(), name='shoping'),
    # 确认订单页面
    path('confirm/', ConfirmView.as_view(), name='confirm'),
    # 确认收货
    path('confirmGoods/', ConfirmGoodsView.as_view(), name='confirmgoods'),
    # 商品评论
    path('commentsGoods', CommentsGoodsView.as_view(), name='commentsgoods'),

    # 购买旅游产品
    path('travelbuy', TravelBuyView.as_view(), name='travelbuy'),
    # 景点评论
    path('commentSpots', CommentsSpotsView.as_view(), name='commentspots'),

    # 搜索功能
    path('search', SearchView.as_view(), name='search'),

]