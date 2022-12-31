from django.contrib import admin
from django.urls import path, include
from ruangan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ruangan.urls')),
    path('dashboard-user/', dashboard_user, name='dashboard'),
    path('peminjaman_barang/', peminjaman_barang, name='barang'),
    path('Peminjaman_ruangan/', peminjaman_ruangan, name='ruangan'),
    path('dashboard_admin/', dashboard_admin, name='dashboard_admin'),
    path('laporan_barang_admin/', peminjaman_barang_admin, name='barang_admin'),
    path('laporan_ruangan_admin/', peminjaman_ruangan_admin, name='ruangan_admin'),
    path('master_barang', master_barang, name='master_barang'),
    path('master_ruangan', master_ruangan, name='master_ruangan')
]
