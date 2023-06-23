from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('delete_comment/<int:id>/', views.delete_comment, name='delete_comment'),
    path('approve_comment/<int:id>/', views.approve_comment, name='approve_comment'),
    path('feature_post/<slug:slug>/', views.feature_post, name='feature_post'),
    path('search/', views.search_posts, name='search_posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
