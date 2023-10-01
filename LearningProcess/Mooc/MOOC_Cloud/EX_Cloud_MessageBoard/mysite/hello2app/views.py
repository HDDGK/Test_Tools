from django.shortcuts import render

# Create your views here.

def hello(request):

    return render(request,'MC_Cloud_EX.html')