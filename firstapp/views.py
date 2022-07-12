from django.shortcuts import render

# Create your views here.

#load first html page
def load_first_page(request):
    return render(request,'first.html')

#load second page
def load_sec_page(request):
    return render(request,'second.html')