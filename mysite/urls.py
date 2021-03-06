"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from polls import views
#mysite/urls 와 polls/urls 로 나눠서 설정할수도있다
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', views.index, name='index'),
    path('polls/<int:question_id>/',views.detail,name='detail'),
    path('polls/<int:question_id>/results/',views.results,name='results'),
    path('polls/<int:question_id>/vote/',views.vote,name='vote'),

    #나누기 수정이 더좋다 확장도 좋아 더 좋은거다
    #path('polls/',include('polls.urls'))
]
