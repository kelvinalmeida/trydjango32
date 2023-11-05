from django.shortcuts import render

from .models import ArticleModel

# Create your views here.
def home(request, *args, **kwargs):

    article_list = ArticleModel.objects.all()

    context = {
        "article_list": article_list
    }

    return render(request, 'articles/home.html', context)