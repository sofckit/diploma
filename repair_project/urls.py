from django.contrib import admin
from django.urls import path
from repairs.views import login_view, add_repair_work, repair_work_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('add_repair_work/', add_repair_work, name='add_repair_work'),
    path('repair_work_list/', repair_work_list, name='repair_work_list'),
]