from django.contrib.auth.models import User
from django.shortcuts import render
from pastebin.models import Paste

def page(request, object_id):
	obj = Paste.objects.get(id=object_id)
	return render(request, 'paste_detail.html', {'object':obj})