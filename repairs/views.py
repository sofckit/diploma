from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import RepairWorkForm
from .models import RepairWork

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_repair_work')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def add_repair_work(request):
    if request.method == 'POST':
        form = RepairWorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repair_work_list')
    else:
        form = RepairWorkForm()
    return render(request, 'add_repair_work.html', {'form': form})

@login_required
def repair_work_list(request):
    repair_works = RepairWork.objects.all()
    return render(request, 'repair_work_list.html', {'repair_works': repair_works})

@login_required
def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Перенаправляем на главную страницу
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def repair_work_stats(request):
    # Получаем текущую дату и время
    now = timezone.now()

    # Статистика за последние 7 дней
    last_week = now - timezone.timedelta(days=7)
    stats_last_week = RepairWork.objects.filter(created_at__gte=last_week).count()

    # Статистика за последние 30 дней
    last_month = now - timezone.timedelta(days=30)
    stats_last_month = RepairWork.objects.filter(created_at__gte=last_month).count()

    # Общая статистика
    total_repair_works = RepairWork.objects.count()

    context = {
        'stats_last_week': stats_last_week,
        'stats_last_month': stats_last_month,
        'total_repair_works': total_repair_works,
    }
    return render(request, 'repair_work_stats.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')  # Перенаправляем на страницу логина
