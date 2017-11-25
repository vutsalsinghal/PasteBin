from django.contrib.auth.models import User
from django.shortcuts import render
from pastebin.models import Paste

def page(request):
	if request.user.is_authenticated():
		object_list = Paste.objects.filter(author=request.user)
	else:
		try:
			TempUser    = User.objects.get(username='TempUser')
			object_list = Paste.objects.filter(author=TempUser)
		except:
			object_list = []
	return render(request, 'paste_list.html', {'object_list':object_list})