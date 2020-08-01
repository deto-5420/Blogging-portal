from django.contrib import admin
from django.urls import path
from .views import post_list,post_detail,post_create,post_update,post_delete
from .views import PostListView  
urlpatterns = [
    path('', post_list, name='home'),
    path('create/',post_create),   
    path('<post_id>/',post_detail),
    path('<post_id>/delete/',post_delete),
    path('<post_id>/update/',post_update)
]


# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView
# )
# from . import views

# urlpatterns = [
#     path('', PostListView.as_view(), name='blog-home'),
#     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
#     path('post/new/', PostCreateView.as_view(), name='post-create'),
#     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),#pk here represent primary key and int make sure only integer value are permitted
#     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
#     path('about/', views.about, name='blog-about'),
# ]