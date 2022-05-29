from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})