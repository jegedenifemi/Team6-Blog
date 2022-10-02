from django.urls import path
from post import views
app_name='post'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>/', views.postDetail, name='post_detail'),
    path('create/', views.createPost, name = 'create_post'),
    path('post/<slug:slug>/delete', views.postDelete, name ='post_delete'),
    path('post/<slug:slug>/update', views.update, name ='post_update'),

]
