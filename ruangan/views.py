from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from ruangan.models import *


def index(request):
    return render(request, 'index.html')


def auth_register(request):
    if request.method == 'GET':
        return render(request, 'auth-register.html')
    if request.method == 'POST':
        # NOTE: Mengambil isi data dari form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Akun Anda Berhasil Di Buat!')
            return redirect('login')
        except Exception as e:
            return HttpResponse(f'{e}')


def auth_login(request):
    if request.method == 'GET':
        return render(request, 'auth-login.html')
    if request.method == 'POST':
        # NOTE: Mengambil isi data dari form
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        try:
            login(request, user)
            return redirect('dashboard')
        except Exception as e:
            return HttpResponse(f'{e}')


def dashboard_user(request):
    return render(request, 'dashboard.html')


def peminjaman_barang(request):
    return render(request, 'barang.html')


def peminjaman_ruangan(request):
    return render(request, 'ruangan.html')


def dashboard_admin(request):
    return render(request, 'admin/dashboard.html')


def peminjaman_barang_admin(request):
    return render(request, 'admin/barang.html')


def peminjaman_ruangan_admin(request):
    return render(request, 'admin/ruangan.html')


def master_barang(request):
    data_barang = Barang.objects.all()
    konteks = {
        'data_barang': data_barang,
    }
    return render(request, 'admin/master_barang.html', konteks)


def master_ruangan(request):
    return render(request, 'admin/master_ruangan.html')
