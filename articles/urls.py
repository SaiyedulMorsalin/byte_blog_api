from django.urls import path
from . import views

urlpatterns = [
    path('articles/list/',views.ArticleAPIView.as_view(),name='article_list')
]

