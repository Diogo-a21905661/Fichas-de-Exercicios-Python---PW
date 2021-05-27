from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'website/home.html')

def about_page_view(request):
    return render(request, 'website/about.html')

def view_page_view(request):
    return render(request, 'website/view.html')