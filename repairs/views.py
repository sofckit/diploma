from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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