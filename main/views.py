from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Page d'acceuil")
    return render(request, 'main/index.html')
