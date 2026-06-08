from django.db import models
from employee.models import Employee


class Attendance(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20
    )

    def __str__(self):
        return f"{self.employee.name} - {self.date}"