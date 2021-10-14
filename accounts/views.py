from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from medicines.models import Medicine
from .forms import UserCreationForm


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"

    def get_success_url(self):
        return reverse(settings.LOGIN_URL)


register_view = RegisterView.as_view()


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect(settings.LOGIN_URL)
    return render(request, "accounts/logout.html", {})


@login_required
def user_detail(request):
    medicines = Medicine.objects.filter(user__username=request.user.username)
    context = {
        'user': request.user,
        'medicines': medicines
    }
    return render(request, 'accounts/detail.html', context=context)
