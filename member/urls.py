from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('htoo', views.htoo, name='htoo'),
    path('shin', views.shin, name='shin'),
    path('zin', views.zin, name='zin'),
    path('yoe', views.yoe, name='yoe'),
    path('kyaw', views.kyaw, name='kyaw'),
    path('zar', views.zar, name='zar'),
]