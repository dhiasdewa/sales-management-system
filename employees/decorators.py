from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from functools import wraps

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return redirect("login")

            if request.user.groups.exists():
                group = request.user.groups.first().name

                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)

            raise PermissionDenied

        return wrapper
    return decorator