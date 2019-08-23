# @Time    : 18-11-20
# @Author  : Zhiqi Kou
# @Email   : zhiqi1028@gmail.com

import xadmin
from xadmin import views
from .models import *


class DiaryAdmin:
    """
    轮播图后台管理
    """
    list_display = ['title']



xadmin.site.register(Diary, DiaryAdmin)
