from django.shortcuts import render, HttpResponse

# Create your views here.

def coming(request):
    return render(request, 'coming_soon.html')
