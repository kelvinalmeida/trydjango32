from django.urls import path


from .views import home, create_article_view

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_article_view, name='create'),
]