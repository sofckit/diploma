from django.contrib import admin
from django.urls import path

from repairs import views
from repairs.views import login_view, add_repair_work, repair_work_list


urlpatterns = [
    path('', views.home_view, name='home'),  # Главная страница
    path('login/', views.login_view, name='login'),
    path('add_repair_work/', views.add_repair_work, name='add_repair_work'),
    path('repair_work_list/', views.repair_work_list, name='repair_work_list'),
path('repair_work_stats/', views.repair_work_stats, name='repair_work_stats'),
    path('logout/', views.logout_view, name='logout'),  # Маршрут для выхода
]