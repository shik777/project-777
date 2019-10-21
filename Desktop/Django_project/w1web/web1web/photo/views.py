from django.conf import settings
from django.shortcuts import render

# Create your views here.

def home(request):

	title = 'welcom'
	

	return render(request, "home.html")