from django.db import models
from django.contrib.auth.models import User


# Recordクラス
class Record(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_text = models.TextField(max_length=1000)
    do_text = models.TextField(max_length=1000, blank=True, null=True)
    check_text = models.TextField(max_length=1000, blank=True, null=True)
    action_text = models.TextField(max_length=1000, blank=True, null=True)
    plan_date = models.DateField(blank=True, null=True)
    do_start = models.DateField(blank=True, null=True)
    do_end = models.DateField(blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)
    action_date = models.DateField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        ordering = ('-plan_date',)

# Topicクラス
class Topic(models.Model):
    title = models.TextField(max_length=100)
    text = models.TextField(max_length=300)
    image = models.TextField(max_length=30)
    genre = models.TextField(max_length=30)
    url = models.TextField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)
