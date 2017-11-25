from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from pastebin.models import Paste
from django import forms
import datetime

def page(request):
	if request.POST:
		form = PasteForm(request.POST)
		if form.is_valid():
			content      = form.cleaned_data['content']
			title        = form.cleaned_data['title']
			syntax       = form.cleaned_data['syntax']
			timestamp    = form.cleaned_data['timestamp']
				
			new_paste = Paste(content=content, title=title, syntax=syntax, timestamp=timestamp)
			new_paste.save()
			return redirect('paste_list')
		else:
			return render(request, 'paste_form.html', {'form':form})
	else:
		form = PasteForm()
	return render(request, 'paste_form.html', {'form':form})

class PasteForm(forms.Form):
	SYNTAX_CHOICES = (('plain', "Choose syntax (default PlainText)"),('python', "Python"),('html', "HTML"),('sql', "SQL"),('javascript', "Javascript"),('css', "CSS"))

	content   = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class':'materialize-textarea','placeholder':'Paste your code here!'}))
	title     = forms.CharField(label="Title", widget=forms.TextInput(attrs={'placeholder':"Title of snippet"}))
	syntax    = forms.ChoiceField(label="Syntax", widget=forms.Select(attrs={'class':'browser-default'}), choices=SYNTAX_CHOICES)
	timestamp = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'readonly':'readonly'}), initial=datetime.date.today)
	def clean(self):
		cleaned_data = super(PasteForm, self).clean()
		return self.cleaned_data