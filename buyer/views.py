from django.shortcuts import render


def home(request):
    return render(request, 'buyer/home.html')