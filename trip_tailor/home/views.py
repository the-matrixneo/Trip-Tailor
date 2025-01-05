from django.shortcuts import render

# Create your views here.

def index(request):
    # Whatever you want to render just render it
    return render(request, 'home/templates/index.html')