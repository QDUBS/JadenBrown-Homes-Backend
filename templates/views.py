
from django.shortcuts import render


def verification_template(request):
    return render(request,"email_verification.html")

def reset_template(request):
    return render(request, "reset_password.html")