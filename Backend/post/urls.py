from django.urls import path
from post import views
app_name='post'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.display_view, name='post_detail')
]
