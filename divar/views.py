from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView,DetailView
from django.http import HttpResponse
from .models import *
# Create your views here.


class FierstView(ListView):
    template_name = 'article_list.html'

    def get_queryset(self):
        return Home.objects.all()


class ArticleDetail(DetailView):
    template_name = 'article_detail.html'

    def get_queryset(self):
        return Home.objects.all()