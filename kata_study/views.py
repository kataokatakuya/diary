from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import PlanForm
from .forms import DoForm
from .forms import CheckForm
from .forms import ActionForm
from .models import Record, Topic
from django.contrib.auth.decorators import login_required
import datetime


def index(request):
    return render(request, 'kata_study/index.html')


@login_required(login_url='/admin/login/')
def plan_post(request):
    if(request.method == 'GET'):
        params = {
            'plan_form': PlanForm(),
        }
        return render(request, 'kata_study/plan_post.html', params)
    elif(request.method == 'POST'):
        owner = request.user
        plan_text = request.POST['plan']
        plan_date = request.POST['plan_date']
        record = Record(owner=owner, plan_text=plan_text, plan_date=plan_date)
        record.save()
        last_data = Record.objects.order_by('id').reverse().first()
        params = {
            'record': last_data,
            'do_form': DoForm(),
        }
        if 'done' in request.POST:
            return render(request, 'kata_study/record.html', params)
        elif 'next' in request.POST:
            return render(request, 'kata_study/do_post.html', params)



@login_required(login_url='/admin/login/')
def do_post(request, num):
    if(request.method == 'POST'):
        data = Record.objects.filter(id=num).first()
        data.do_start = makedate(request.POST['do_start'])
        data.do_end = makedate(request.POST['do_end'])
        data.do_text = request.POST['do']
        data.save()
        params = {
            'do_form': PlanForm(),
            'record': data,
        }
        return render(request, 'kata_study/record.html', params)



@login_required(login_url='/admin/login/')
def history(request, num=1):
    data = Record.objects.filter(owner=request.user)
    page = Paginator(data, 3)
    params = {
        'histories': page.get_page(num),
    }
    return render(request, 'kata_study/history.html', params)

@login_required(login_url='/admin/login/')
def record(request, num):
    data = Record.objects.filter(id=num).first()
    params = {
        'record': data
    }
    return render(request, 'kata_study/record.html', params)


@login_required(login_url='/admin/login/')
def edit(request, num):
    data = Record.objects.get(id=num)
    if request.method == "GET":
        params = {
            'plan_form': PlanForm({
                'plan_date': data.plan_date,
                'plan': data.plan_text,
                }),
            'do_form': DoForm({
                'do_start': data.do_start,
                'do_end': data.do_end,
                'do': data.do_text,
            }),
            'check_form': CheckForm({
                'check_date': data.check_date,
                'check': data.check_text,
            }),
            'action_form': ActionForm({
                'action_date': data.action_date,
                'action': data.action_text,
            }),
            'record': data,
        }
        template_name = "kata_study/edit.html"
    
    if request.method == "POST":
        if request.POST['plan_date'] != '':
            data.plan_date = makedate(request.POST['plan_date'])
        if request.POST['plan'] != '':
            data.plan_text = request.POST['plan']
        if request.POST['do_start'] != '':
            data.do_start = makedate(request.POST['do_start'])
        if request.POST['do_end'] != '':
            data.do_end = makedate(request.POST['do_end'])
        if request.POST['do'] != '':
            data.do_text = request.POST['do']
        if request.POST['check_date'] != '':
            data.check_date = makedate(request.POST['check_date'])
        if request.POST['check'] != '':
            data.check_text = request.POST['check']
        if request.POST['action_date'] != '':
            data.action_date = makedate(request.POST['action_date'])
        if request.POST['action'] != '':
            data.action_text = request.POST['action']        
        data.save()
        template_name = "kata_study/record.html"
        params = {
            'record': data
        }
    return render(request, template_name, params)


# 引数として与えられた文字列をdatetimeクラスにして呼び出し元に返却する
def makedate(str):
    str = str.replace('-', '')
    date = datetime.date(int(str[0:4]), int(str[4:6]), int(str[6:8]))
    return date


@login_required(login_url='/admin/login/')
def delete(request, num):
    target = Record.objects.get(id=num)
    target.delete()
    data = Record.objects.filter(owner=request.user)
    page = Paginator(data, 3)
    params = {
        'histories': page.get_page(1),
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


# 単回帰ページの表示
def smp_reg(request):
    params = {
        'graph': '',
        'coefficients': '',
        'intercept':'',
        'score': '',
        'result_title': ''
    }
    # # 単回帰ページにて「単回帰の実行」ボタンを押下時
    # if (request.method == 'POST'):
    #     model_data = smp_learn()
    #     params['graph'] = '/report/smp_reg/smp_plot'
    #     params['coefficients'] = model_data['coefficients']
    #     params['intercept'] = model_data['intercept']
    #     params['score'] = model_data['score']
    #     params['result_title'] = "【実行結果】"
    return render(request, 'kata_study/smp_reg.html', params)


# 重回帰ページの表示
def multi_reg(request):
    flg = ""
    params = {
        'coefficients': '',
        'intercept':'',
        'score': '',
        'result_title': '',
        'flg': flg
    }
    # if (request.method == 'POST'):
    #     model_data = multi_learn()
    #     params['coefficients'] = model_data['coefficients'].to_html()
    #     params['intercept'] = model_data['intercept']
    #     params['score'] = model_data['score']
    #     params['result_title'] = "【実行結果】"
    #     params['flg'] = "Y"
    return render(request, 'kata_study/multi_reg.html', params)