from django.shortcuts import render

# Create your views here.
def simple(request):
    return render(request, "index.html", {})