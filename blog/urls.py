from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/comment', views.post_comment, name='comment'),
]
