from django.urls import re_path
from .views import (question_list, 
                    question_detail, 
                    question_ask, 
                    question_update, 
                    category_list, 
                    category,
                    answer_update,
                    question_delete,
                    answer_delete,
                    notification)

app_name = 'questions'


urlpatterns = [
    re_path(r'^$', question_list, name='question_list'),
    re_path(r'^ask/$', question_ask, name='question_ask'),
    re_path(r'^notifications/$', notification, name='notification'),
    re_path(r'^categories/$', category_list, name='category_list'),
    re_path(r'^categories/(?P<slug>[\w-]+)/$', category, name='category'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', question_delete, name='question_delete'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', question_update, name='question_update'),
    re_path(r'^(?P<slug>[\w-]+)/answer/(?P<pk>\d+)/edit/$', answer_update, name='answer_update'),
    re_path(r'^(?P<slug>[\w-]+)/answer/(?P<pk>\d+)/delete/$', answer_delete, name='answer_delete'),
    re_path(r'^(?P<slug>[\w-]+)/$', question_detail, name='question_detail'),
    ]