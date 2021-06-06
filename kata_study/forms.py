from django import forms

class PlanForm(forms.Form):
    plan_date = forms.DateField(label='計画日',\
        widget=forms.DateInput(attrs={'class': 'form-control',"type":"date"}))
    plan = forms.CharField(max_length=1000, label='計画内容', \
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))


class DoForm(forms.Form):
    do_start = forms.DateField(label='実行期間(開始日)', required=False, \
        widget=forms.DateInput(attrs={'class': 'form-control',"type":"date"}))
    do_end = forms.DateField(label='実行期間(終了日)', required=False, \
        widget=forms.DateInput(attrs={'class': 'form-control',"type":"date"}))
    do = forms.CharField(max_length=1000, label='実行内容', required=False, \
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))


class CheckForm(forms.Form):
    check_date = forms.DateField(label='評価日', required=False, \
        widget=forms.DateInput(attrs={'class': 'form-control',"type":"date"}))
    check = forms.CharField(max_length=1000, label='評価内容', required=False, \
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))


class ActionForm(forms.Form):
    action_date = forms.DateField(label='改善開始日', required=False, \
        widget=forms.DateInput(attrs={'class': 'form-control',"type":"date"}))
    action = forms.CharField(max_length=1000, label='改善内容', required=False, \
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))