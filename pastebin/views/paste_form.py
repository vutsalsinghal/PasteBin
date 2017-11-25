from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from pastebin.models import Paste
from django.conf import settings
from django import forms
import datetime

def page(request):
	if request.POST:
		form = PasteForm(request.POST)
		if request.user.is_authenticated():
			user_obj = User.objects.get(username=request.user)
		else:
			try:
				user_obj = User.objects.get(username='TempUser')
			except:
				# Create a dummy user
				user_obj = User.objects.create_user(username='TempUser', password='TempUser')
				user_obj.is_active  = False
				user_obj.is_staff   = False
				user_obj.first_name = 'Temp User'
				user_obj.save()

		if form.is_valid():
			content    = form.cleaned_data['content']
			title      = form.cleaned_data['title']
			syntax     = form.cleaned_data['syntax']
			createDate = form.cleaned_data['createDate']
			expiryDate = form.cleaned_data['expiryDate']
				
			new_paste = Paste(author=user_obj, content=content, title=title, syntax=syntax, createDate=createDate, expiryDate=expiryDate)
			new_paste.save()
			return redirect('paste_detail/' + str(new_paste.id) + '/')
		else:
			return render(request, 'paste_form.html', {'form':form})
	else:
		form = PasteForm()
	return render(request, 'paste_form.html', {'form':form})

class PasteForm(forms.Form):
	SYNTAX_CHOICES = (('plain', "Choose syntax (default PlainText)"),('python', "Python"),('html', "HTML"),('sql', "SQL"),('javascript', "Javascript"),('css', "CSS"))

	content    = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class':'materialize-textarea','placeholder':'Paste your code here!'}))
	title      = forms.CharField(label="Title", widget=forms.TextInput(attrs={'placeholder':"Title of snippet"}))
	syntax     = forms.ChoiceField(label="Syntax", widget=forms.Select(attrs={'class':'browser-default'}), choices=SYNTAX_CHOICES)
	createDate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'readonly':'readonly'}), initial=datetime.date.today)
	expiryDate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'readonly':'readonly'}), initial=(datetime.date.today() + datetime.timedelta(days=settings.EXPIRY_DAYS)))
	def clean(self):
		cleaned_data = super(PasteForm, self).clean()
		return self.cleaned_data