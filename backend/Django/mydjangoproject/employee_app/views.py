from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_app/register.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_app/list.html', {'employees': employees})

def employee_info(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'employee_app/info.html', {'employee': employee})

def employee_edit(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_app/edit.html', {'form': form})

def employee_delete(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_app/delete.html', {'employee': employee})