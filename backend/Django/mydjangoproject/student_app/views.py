from django.shortcuts import render, redirect,get_object_or_404
from .forms import StudentRegistrationForm
from .models import Student

# Student List Page
def student_list(request):
    students=Student.objects.all()
    return render(request, 'student_app/index.html',{'students':students})


# Student Form Page
def student_form(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_details', pk=student.pk)
    else:
        form = StudentRegistrationForm()

    return render(request, 'student_app/form.html', {'form': form})


# Student Info Page
def student_info(request, pk):
    student=get_object_or_404(Student,pk=pk)
    return render(request, 'student_app/info.html',{'student':student})

# Student Edit Page
def student_edit(request, pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_details', pk=student.pk)
    else:
        form = StudentRegistrationForm(instance=student)
    return render(request, 'student_app/form.html', {'form': form})

# Student Delete Page
def student_delete(request, pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_app/delete.html', {'student': student})