from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Record, Topic


def index(request):
    return render(request, 'kata_study/index.html')

# 機械学習リストページの表示
def mch(request, num=1):
    data = Topic.objects.filter()
    page = Paginator(data, 4)
    params = {
        'topics': page.get_page(num),
    }
    return render(request, 'kata_study/mch_list.html', params)