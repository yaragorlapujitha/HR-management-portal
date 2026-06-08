from django.db import models
from employee.models import Employee


class Payroll(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    basic_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    bonus = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    deductions = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    net_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.employee.name
