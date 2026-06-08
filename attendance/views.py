from django.shortcuts import render, redirect
from employee.models import Employee
from .models import Attendance


def attendance_add(request):

    employees = Employee.objects.all()

    if request.method == "POST":

        Attendance.objects.create(
            employee_id=request.POST['employee'],
            date=request.POST['date'],
            status=request.POST['status']
        )

        return redirect('/attendance/list/')

    return render(
        request,
        'attendance/add.html',
        {'employees': employees}
    )
def attendance_list(request):
    attendances = Attendance.objects.all()

    return render(
        request,
        'attendance/list.html',
        {'attendances': attendances}
    )