
from django.contrib import admin
from django.urls import path, include
from account.views import account_view, teacher_view
# from account.views import logout_view, login_view
from django.conf import settings
from django.conf.urls.static import static
# from account.views import HomeView
from django.contrib.auth import views as auth_views
from account.views import LogoutConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),


    path('account/', include('account.urls')),
    # path('account/', include('django.contrib.auth.urls')),
    # path('logout/', logout_view, name='logout'),
    # path('login/', login_view, name='login'),

    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout_confirm/', LogoutConfirmView.as_view(), name='logout_confirm'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('defupdate/', account_view, name='def-update'),

    path('users/', include('users.urls')),


    path('teacher/', include('teacher.urls')),
    path('classroom/', include('classroom.urls')),
    path('', include('course.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
