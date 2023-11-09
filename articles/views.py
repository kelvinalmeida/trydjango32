from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ArticleModel
from .forms import ArticleForm


# Create your views here.
def home(request, *args, **kwargs):

    article_list = ArticleModel.objects.all()

    context = {
        "article_list": article_list
    }

    return render(request, 'articles/home.html', context)


@login_required
def create_article_view(request, *args, **kwargs):
    
    form = ArticleForm(request.POST or None)
    # print(dir(form))
    context = {
        "form": form
    }

    if form.is_valid():
        article_obj = form.save()
        form = ArticleForm()
        context['form'] = form
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # object_article = ArticleModel.objects.create(title=title , content=content)

    return render(request, 'articles/create.html', context)

# @login_required
# def create_article_view(request, *args, **kwargs):
#     print(request.POST)
#     context = {
#         "object": None
#     }

#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         object_article = ArticleModel.objects.create(title=title , content=content)
#         print(object_article)
#         context = {
#             "object": object_article
#         }

#     return render(request, 'articles/create.html', context)