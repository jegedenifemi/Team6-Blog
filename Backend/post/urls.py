from django.urls import path
from post import views
app_name='post'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.display_view, name='post_detail'),
    path('create_new_post/', views.createPost, name = 'create_post'),
]
