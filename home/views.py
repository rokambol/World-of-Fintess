from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displey index.html"""
    return render(request, "index.html")
