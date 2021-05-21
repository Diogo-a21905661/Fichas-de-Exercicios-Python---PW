#  hello/views.py

from django.shortcuts import render

def home_page_view(request):
	return render(request, 'website/home.html')

def base_page_view(request):
	return render(request, 'website/base.html')

def crash_page_view(request):
	return render(request, 'website/crash.html')

def door_page_view(request):
	return render(request, 'website/door.html')