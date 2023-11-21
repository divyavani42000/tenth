from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'divya'}
    return render(request,'forloop.html',d)