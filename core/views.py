from django.shortcuts import render

# Create your views here.
def index(request):
    context={'text':0.0}
    return render(request,'core/index.html',context)