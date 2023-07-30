from django.shortcuts import render,HttpResponse

# Create your views here.
def roger(request):
    return HttpResponse("this is epic.")

