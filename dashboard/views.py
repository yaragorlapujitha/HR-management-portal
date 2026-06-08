from django.shortcuts import render
from employee.models import Employee
from attendance.models import Attendance
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_home(request):

    total_employees = Employee.objects.count()

    total_attendance = Attendance.objects.count()

    total_present = Attendance.objects.filter(
        status='Present'
    ).count()

    total_absent = Attendance.objects.filter(
        status='Absent'
    ).count()

    context = {
        'total_employees': total_employees,
        'total_attendance': total_attendance,
        'total_present': total_present,
        'total_absent': total_absent,
    }

    return render(
        request,
        'dashboard/home.html',
        context
    )