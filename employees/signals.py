from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Employee
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchase, Sale

User = get_user_model()


@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)


@receiver(post_save, sender=Purchase)
def update_stock_on_purchase(sender, instance, created, **kwargs):
        if created:
            product = instance.product
            product.stock += instance.quantity
            product.save()


@receiver(post_save, sender=Sale)
def update_stock_on_sale(sender, instance, created, **kwargs):
        if created:
            product = instance.product
            product.stock -= instance.quantity
            product.save()


@receiver(post_save, sender=Sale)
def reduce_stock_on_sale(sender, instance, created, **kwargs):
    if created:
        print("SALE SIGNAL JALAN 🔥")
        product = instance.product
        product.stock -= instance.quantity
        product.save()

@receiver(post_save, sender=Purchase)
def increase_stock_on_purchase(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.stock += instance.quantity
        product.save()
