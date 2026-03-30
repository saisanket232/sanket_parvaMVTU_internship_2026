from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegistrationForm

def home(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentRegistrationForm()

    return render(request, 'demo/index.html', {'form': form})

def greet(request):
    return render(request, 'demo/greet.html')

def bye(request):
    return render(request, 'demo/bye.html')