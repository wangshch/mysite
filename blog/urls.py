from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<pk>/', views.PostDetailView.as_view(), name='detail'),
    path('archives/<year>/<month>/', views.ArchivesView.as_view(), name='archives'),
    path('category/<pk>/', views.CategoryView.as_view(), name='category'),
    path('tag/(<pk>/', views.TagView.as_view(), name='tag'),
]
