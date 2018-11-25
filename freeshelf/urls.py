"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from books import views



urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.index, name='book_list'),
    path('books/<slug>/', views.book_detail, name='book_detail'),
    path('category/python/',views.python, name='python'),
    path('category/css/',views.css, name='css'),
    path('category/html/',views.html, name='html'),
    path('category/javascript/',views.javascript, name='javascript'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/password/reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name='password_reset'),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/password/done/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
