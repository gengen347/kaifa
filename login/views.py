from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return HttpResponse('<h1>测试开发8期的大佬大家好！</h1>')


def get_project(request):
    return HttpResponse('<h1>这是某某项目</h1>')


def get_project_by_id(request, ids):
    if isinstance(ids, int) and ids < 100:
        return HttpResponse(f'这是id为{ids}的项目')
    else:
        return HttpResponse(f'id为{ids}的项目不存在')


def get_users(request, username):
    pass
