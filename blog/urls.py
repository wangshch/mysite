from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<pk>/', views.detail, name='detail'),
    path('archives/<year>/<month>/', views.archives, name='archives'),
    path('category/<pk>/', views.category, name='category'),
]
