from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.contrib.auth.decorators import login_required


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list.html', {'employees': employees})


@login_required
def employee_add(request):

    if request.method == "POST":

        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            department=request.POST['department'],
            salary=request.POST['salary']
        )

        return redirect('/employee/')

    return render(request, 'employee/add.html')


@login_required
def employee_edit(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']

        employee.save()

        return redirect('/employee/')

    return render(request, 'employee/edit.html', {'employee': employee})


@login_required
def employee_delete(request, id):

    employee = get_object_or_404(Employee, id=id)
    employee.delete()

    return redirect('/employee/')