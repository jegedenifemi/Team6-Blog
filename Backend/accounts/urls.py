from django.urls import path
from accounts import views
urlpatterns = [
    path('login/', views._log_in, name = 'login'),
    path('logout/', views._log_out, name = 'logout'),
    path('signup/', views._sign_up, name = 'signup'),
    path('', views.index, name='index'),
]