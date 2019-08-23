# @Time    : 18-10-24
# @Author  : Zhiqi Kou
# @Email   : zhiqi1028@gmail.com


from django.urls import path, re_path,include
from .views import *

urlpatterns = [
    # 写游记页面
    path('getdiaray/<int:diary_id>/', GetdiarayView.as_view(), name='getdiaray'),
    # 修改游记
    path('setdiaray/<slug:operation_type>/<int:diary_id>/', SetdiarayView.as_view(), name='setdiaray'),
    # 游记详情
    path('details/<int:diary_id>/', DetailsView.as_view(), name='details'),
    # 用户的游记，已发表游记/草稿
    path('mydetails/<slug:is_published>/', MyDetailsView.as_view(), name='mydetails'),
    # 游记发表
    path('publish/<int:diary_id>/', PublishView.as_view(), name='publish'),
    # 游记删除
    path('delete/', DeleteView.as_view(), name='delete'),

    path('all/<slug:diary_type>/', AllDiaryView.as_view(), name='all')
]