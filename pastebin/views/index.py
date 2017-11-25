from django.shortcuts import render
#from pastebin.models import UserProfile

def page(request):
	return render(request, 'index.html',{})