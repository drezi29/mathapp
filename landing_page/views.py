from django.shortcuts import render


def landing_page(request):
    return render(request, 'landing_page/home.html')


def credits_page(request):
    return render(request, 'landing_page/credits.html')
