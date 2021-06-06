from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Record, Topic


def index(request):
    return render(request, 'kata_study/index.html')


def history(request, num=1):
    data = Record.objects.filter(owner=request.user)
    page = Paginator(data, 3)
    params = {
        'histories': page.get_page(num),
    }
    return render(request, 'kata_study/history.html', params)


# 機械学習リストページの表示
def mch(request, num=1):
    data = Topic.objects.filter()
    page = Paginator(data, 4)
    params = {
        'topics': page.get_page(num),
    }
    return render(request, 'kata_study/mch_list.html', params)