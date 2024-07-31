"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path as url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from profiles import urls as profiles_urls
from feed import urls as feed_urls
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),# new 
    path("",include(feed_urls,namespace="feed")),
    path("profile/",include(profiles_urls,namespace="profiles")),
    url("",include("allauth.urls")),
    path('', include('django.contrib.auth.urls')),
    path("login/",views.login_page,name="login"),
    path("register/",views.register_page,name="register"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
