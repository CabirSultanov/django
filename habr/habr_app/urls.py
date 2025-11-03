from django.urls import path
from . import views

app_name = 'habr_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('add/', views.add_article, name='add_article'),
    path('article/<int:article_id>/like/', views.like_article, name='like_article'),
    path('article/<int:article_id>/dislike/', views.dislike_article, name='dislike_article'),
]
