"""django_start URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from webdriver_service.django_start.django_start.view import changeModel, changeModelBatch
from webdriver_service.django_start.manage import hello
from django.conf.urls import url

urlpatterns = [
    url(r"test.go", hello),
    url(r"fapiao.go", changeModel),
    url(r"zhongdeng.go", changeModel),
    url(r"zhongdengdengji.go", changeModel),
    url(r"fapiaoList.go", changeModelBatch),
]
