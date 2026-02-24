from django.contrib import admin
from .models import Employee
from .models import Product
from .models import Purchase, Sale
from .models import ActivityLog



class EmployeeAdmin(admin.ModelAdmin):

    # ===== MODULE ACCESS =====
    def has_module_permission(self, request):
        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        if hasattr(request.user, "role") and request.user.role:
            return True

        return False


    # ===== VIEW PERMISSION =====
    def has_view_permission(self, request, obj=None):
        return self.has_module_permission(request)


    # ===== ADD PERMISSION =====
    def has_add_permission(self, request):
        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        if hasattr(request.user, "role") and request.user.role:
            if request.user.role.name == "HR":
                return True

        return False


    # ===== CHANGE PERMISSION =====
    def has_change_permission(self, request, obj=None):
        return self.has_add_permission(request)


    # ===== DELETE PERMISSION =====
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


    # ===== OBJECT LEVEL FILTER =====
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_authenticated:
            return queryset.none()

        if request.user.is_superuser:
            return queryset

        if hasattr(request.user, "role") and request.user.role:
            if request.user.role.name == "HR":
                return queryset

            if request.user.role.name == "Employee":
                return queryset.filter(user=request.user)

        return queryset.none()


    # ===== FIELD LEVEL PERMISSION =====
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if hasattr(request.user, "role") and request.user.role:
            if request.user.role.name == "Employee":
                if "salary" in form.base_fields:
                    form.base_fields.pop("salary")

        return form


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Sale)
admin.site.register(ActivityLog)
