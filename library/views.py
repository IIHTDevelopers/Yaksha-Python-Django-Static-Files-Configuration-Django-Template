from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # This will serve the home page where static files are included
