from django.shortcuts import render
from app import models


# Create your views here.

def index(request):
    return render(request, 'index.html')


def startWechat(request):
    return render(request, 'redirect.html')


def article(request):
    article_type_list = models.ArticleType.objects.all()
    category_list = models.Category.objects.all()
    article_list = models.Article.objects.all()
    return render(request, 'article.html', {
        'article_type_list': article_type_list,
        'category_list': category_list,
        'article_list': article_list
    })
