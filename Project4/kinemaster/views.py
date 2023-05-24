from django.shortcuts import render

# Create your views here.
def kinemaster(request):
    d={'name':'abi','age':'20'}
    return render(request,'kinemaster.html',d)