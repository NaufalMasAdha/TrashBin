from django.shortcuts import render
from .models import Deskripsi
from .models import Peta
from django.http import HttpResponse

# Create your views here.
def keterangan_list(request):
    return render(request, 'keterangan/keterangan_list.html')

def peta_baiturrahman(request):
    return render(request, 'keterangan_peta/Baiturrahman.html')

def peta_banda_raya(request):
    return render(request, 'keterangan_peta/Banda_Raya.html')

def peta_jaya_baru(request):
    return render(request, 'keterangan_peta/Jaya_Baru.html')

def peta_kuta_alam(request):
    return render(request, 'keterangan_peta/Kuta_alam.html')

def peta_kuta_raja(request):
    return render(request, 'keterangan_peta/Kuta_raja.html')

def peta_lueng_bata(request):
    return render(request, 'keterangan_peta/peta_Lueng_batahtml')

def peta_meuraxa(request):
    return render(request, 'keterangan_peta/peta_Meuraxa.html')

def peta_syiah_kuala(request):
    return render(request, 'keterangan_peta/peta_Syiah_Kuala.html')

def peta_ulee_kareng(request):
    return render(request, 'keterangan_peta/peta_Uleee_Kareng.html')
