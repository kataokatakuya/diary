from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mch', views.mch, name='mch'),
    path('mch/<int:num>', views.mch, name='mch'),
]