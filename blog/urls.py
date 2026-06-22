from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
   path('', views.home, name='home'),
   # path('post/<int:id>/', views.post_detail, name='post_detail'),
   path('article/<int:article_id>/', views.article_detail, name='article_detail'),
   path('authors/', views.authors_stats, name='authors_stats'),
   path('search/', views.search, name='search')
]