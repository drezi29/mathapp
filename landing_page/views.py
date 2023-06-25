from django.shortcuts import render

def testing(request):
    return render(request, 'landing_page/home.html')
