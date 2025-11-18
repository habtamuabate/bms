from django.urls import path
from . import views

app_name = 'bid_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/', views.project_list, name='project_list'),
    path('bids/', views.bid_list, name='bid_list'),
]