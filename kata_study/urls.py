from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plan_post', views.plan_post, name='post'),
    path('posted', views.plan_post, name='plan_posted'),
    path('posted/<int:num>', views.do_post, name='do_posted'),
    path('mch', views.mch, name='mch'),
    path('mch/<int:num>', views.mch, name='mch'),
    path('smp_reg', views.smp_reg, name='smp_reg'),
    # path('smp_reg/smp_plot', views.smp_get_svg, name='smp_plot'),
    path('history', views.history, name='history'),
    path('history/<int:num>', views.history, name='history'),
    path('record/<int:num>', views.record, name='record'),
    path('record/edit/<int:num>/', views.edit, name='edit'),
    path('record/delete/<int:num>/', views.delete, name='delete'),
]