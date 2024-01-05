# -*- coding: utf-8 -*-

from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('index2/', views.index2, name='index2'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]

