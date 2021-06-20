from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def sign_upview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/accounts/sign_in/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign_up.html', {'form':form})


def sign_inview(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request, user)
            return redirect('/pelaporan/pesan_pelaporan')

    else:
       form = AuthenticationForm()
    return render(request, 'accounts/sign_in.html', {'form':form})

def sign_outview(request):
    if request.method=='POST':
        logout(request)
    return redirect('http://127.0.0.1:8000/')
