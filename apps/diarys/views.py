from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.urls import reverse

import json


from .models import *
from operation.models import UserFav,UserCollect, DiaryComments
from .forms import *


# Create your views here.
class GetdiarayView(View):
    """
    编写游记页面
    """
    def get(self, request, diary_id):

        if diary_id == 0:
            return render(request, 'write_note.html', {
                'image': 'diary/default.jpg',
            })
        else:
            diary = Diary.objects.get(id=diary_id, user=request.user)
            image = diary.image

            return render(request, 'write_note.html', {
                'diary': diary,
                'image': image,
            })


class SetdiarayView(View):
    """
    提交游记
    """
    def post(self, request, operation_type, diary_id):
        if diary_id == 0:
            # 新建游记
            diary = Diary()
            diary.user = request.user
            diary.title = request.POST.get('title', '')
            diary.image = request.FILES.get('image', '')
            diary.content = request.POST.get('content', '')
            if operation_type == 'express':
                diary.is_published = True
            elif operation_type == 'save':
                diary.is_published = False
            else:
                # 错误
                pass
            diary.save()
            # 获得最后一篇游记并返回
            editor_diary = request.user.diary_set.all().order_by('-add_times')[0]
        else:
            # 编辑游记
            diary = Diary.objects.get(id=diary_id, user=request.user)
            diary.title = request.POST.get('title', '')
            diary.image = request.FILES.get('image', '')
            diary.content = request.POST.get('content', '')
            if operation_type == 'express':
                diary.is_published = True
            elif operation_type == 'save':
                diary.is_published = False
            else:
                # 错误
                pass
            diary.save()
            # 获得最后一篇游记并返回
            editor_diary = Diary.objects.get(id=diary_id, user=request.user)
        return HttpResponseRedirect(reverse('diarys:getdiaray', kwargs={'diary_id': editor_diary.id}))


class MyDetailsView(View):
    """
    当前登陆用户已发表游记
    """
    def get(self, request, is_published):
        all_diary = request.user.diary_set.all().order_by('-add_times')
        diarys = []
        if is_published == 'published':
            diarys = all_diary.filter(is_published=True)
        elif is_published == 'draft':
            diarys = all_diary.filter(is_published=False)
        else:
            # 错误
            pass

        return render(request, 'my_note.html', {
            'diarys': diarys,
            'is_published': is_published,
        })


class PublishView(View):
    """
    游记发表
    """
    def get(self, request, diary_id):
        new_diarys = request.user.diary_set.all()
        diary = new_diarys.get(id=diary_id)
        diary.is_published = True
        diary.save()
        return HttpResponseRedirect(reverse('diarys:details', kwargs={'diary_id': diary_id}))


class DetailsView(View):
    """
    游记详情
    """
    def get(self, request, diary_id):
        # new_diarys = request.user.diary_set.all().filter(is_published=True).order_by('-add_times')[:6]
        diary = Diary.objects.get(id=diary_id)
        diary.checknum += 1
        diary.save()

        comm_diarys = DiaryComments.objects.filter(diary=diary).order_by('-add_time')

        try:
            fav_diary = UserFav.objects.get(diary=diary, user=request.user)
            hasfav = True
        except:
            hasfav = False

        try:
            coll_diary = UserCollect.objects.get(diary=diary, user=request.user)
            hascoll = True
        except:
            hascoll = False

        return render(request, 'note.html', {
            'diary': diary,
            # 'new_diarys': new_diarys,
            'hasfav': hasfav,
            'hascoll': hascoll,
            'comm_diarys': comm_diarys,
            'now_type': 'diary',
        })


class DeleteView(View):
    """
    删除游记
    """
    def post(self, request):
        diary_id = request.POST.get('id', '')
        new_diarys = request.user.diary_set.all()
        diary = new_diarys.get(id=diary_id)
        diary.delete()
        result = json.dumps({"status": "success"}, ensure_ascii=False)
        return HttpResponse(result)


class AllDiaryView(View):
    """
    所有游记
    """
    def get(self, request, diary_type):
        diarys = []
        if diary_type == 'new':
            diarys = Diary.objects.all().order_by("-add_times")
        elif diary_type == 'hot':
            diarys = Diary.objects.all().order_by("-praisenum")
        else:
            # 链接错误！
            pass

        return render(request, 'note_list.html', {
            'diarys': diarys,
            'diary_type': diary_type,
            'now_type': 'diary',
        })