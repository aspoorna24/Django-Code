from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('page',views.page, name='page'),
    path('add',views.add, name='add'),
    path('adds',views.adds,name='adds')
]