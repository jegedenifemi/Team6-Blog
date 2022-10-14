from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from .forms import PwdChangeForm
urlpatterns = [
    path('login/', views._log_in, name = 'login'),
    path('logout/', views._log_out, name = 'logout'),
    path('signup/', views._sign_up, name = 'signup'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='accounts/pwd_changeform.html',
                                                form_class =PwdChangeForm), name = 'pwdchange'),
    path('password-reset/',views.password_reset_request,name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),  
    path('bookmarks/<int:id>',views.bookmarks_Add, name = 'bookmarks_add' )
]  
