from django.urls import path
from . import views
from .views import index, remove_background 

urlpatterns = [
    path('', views.index, name='index'),
    path('imaginify/', views.remove_background, name='remove-background')
]
