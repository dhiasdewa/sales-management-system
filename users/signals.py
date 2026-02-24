from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from employees.models import Employee
from .models import Role


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        try:
            employee_role = Role.objects.get(name="Employee")
            if instance.role == employee_role:
                Employee.objects.create(
                    user=instance,
                    employee_id=f"EMP{instance.id:04d}",
                    phone="",
                    address="",
                    position="Staff",
                    hire_date="2025-01-01"
                )
        except Role.DoesNotExist:
            pass