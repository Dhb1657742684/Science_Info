from django.shortcuts import render


def index(request):
    return render(request, 'buyer/index.html')


def base(request):
    return render(request, 'buyer/base.html')


def register(request):
    return render(request, 'buyer/register.html')


def login(request):
    return render(request, 'buyer/login.html')

# Create your views here.
