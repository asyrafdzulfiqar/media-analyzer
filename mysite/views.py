from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "mysite/index.html")

def _chat(request):
    if request.method == "POST":
        print(request.POST)
        
    else:
        return HttpResponse("hi")