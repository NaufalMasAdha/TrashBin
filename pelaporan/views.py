from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pelaporan
from. import forms


# Create your views here.
def Laporan_berhasil(request):
    return render(request, 'pelaporan/Laporan_berhasil.html')


@login_required(login_url="/accounts/sign_in/")
def pesan_pelaporan(request):
    if request.method=='POST':
        form=forms.BuatLaporan(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.Pelapor = request.user
            instance.save()
        return redirect('/pelaporan/laporan_berhasil/')
    else:
        form =forms.BuatLaporan()
    return render(request, 'pelaporan/pesan_pelaporan.html' ,{'form':form})
