from django.urls import path
from . import views

app_name = 'adtaa'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addCourse, name='add')


]