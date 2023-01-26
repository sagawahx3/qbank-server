"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from question.views import QuestionViewSet
from userinfo.views import UserInfoViewSet
from rest_framework import routers
from django.urls import re_path as url
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_str as force_text

router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('', include(router.urls)),
    path('userinfo/<int:pk>/', UserInfoViewSet.get_object),

]
