from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employee.models import Employee
from .models import Payroll


@login_required
def payroll_add(request):

    employees = Employee.objects.all()

    if request.method == "POST":

        basic_salary = float(request.POST['basic_salary'])
        bonus = float(request.POST['bonus'])
        deductions = float(request.POST['deductions'])

        net_salary = basic_salary + bonus - deductions

        Payroll.objects.create(
            employee_id=request.POST['employee'],
            basic_salary=basic_salary,
            bonus=bonus,
            deductions=deductions,
            net_salary=net_salary
        )

        return redirect('/payroll/list/')

    return render(
        request,
        'payroll/add.html',
        {'employees': employees}
    )


@login_required
def payroll_list(request):

    payrolls = Payroll.objects.all()

    return render(
        request,
        'payroll/list.html',
        {'payrolls': payrolls}
    )