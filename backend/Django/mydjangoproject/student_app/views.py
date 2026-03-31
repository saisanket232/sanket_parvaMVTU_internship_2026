from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm


# Student List Page
def student_list(request):
    return render(request, 'student_app/index.html')


# Student Form Page
def student_form(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_info')
    else:
        form = StudentRegistrationForm()

    return render(request, 'student_app/form.html', {'form': form})


# Student Info Page
def student_info(request):
    return render(request, 'student_app/info.html')