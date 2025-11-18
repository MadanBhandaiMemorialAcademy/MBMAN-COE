from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render


def login(request):
    """Login view"""
    if request.user.is_authenticated:
        return redirect("home:index")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            # Redirect staff/admin to admin dashboard
            if user.is_staff or user.is_superuser:
                next_url = request.GET.get("next", "home:admin_dashboard")
            else:
                next_url = request.GET.get("next", "home:index")
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "auth/login.html")


def logout(request):
    """Logout view"""
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("home:index")
