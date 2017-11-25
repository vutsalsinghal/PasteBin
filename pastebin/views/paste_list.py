from django.contrib.auth.models import User
from django.shortcuts import render
from pastebin.models import Paste

def page(request):
	object_list = Paste.objects.all()
	return render(request, 'paste_list.html', {'object_list':object_list})