from django.shortcuts import render


def welcome_page(request):
    return render(request, 'welcome_page.html')

from django.shortcuts import render


