from django.shortcuts import render, redirect
from .forms import UserDataForm
from .models import UserData

def home(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserDataForm()

    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')

