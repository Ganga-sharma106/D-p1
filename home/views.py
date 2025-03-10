from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    # context={
    #     'value1': 'this is my first value'
    # }
    return render(request,"index.html")
    # return HttpResponse("This is Home Page")
    

def about(request):
     return render(request,"about.html")
    # return HttpResponse("This is About Page")

def services(request):
     return render(request,"services.html")
    # return HttpResponse("This is Service Page")

def contact(request):
     return render(request,"contact.html")
    # return HttpResponse("This is Contact Page")
