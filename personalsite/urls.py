"""personalsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from account.views import RegisterView, AccountLoginView, DashboardView
urlpatterns = [
    path('user/admin/', admin.site.urls),
    path('', include('website.urls')),
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/login/', AccountLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('user/logout/', LogoutView.as_view(), name='logout'),
    path('user/profile/',DashboardView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
