from django.contrib.auth.models import User
from django.db.models import permalink
from django.contrib import admin
from django.db import models
import datetime

class Paste(models.Model):
	SYNTAX_CHOICES = (('plain', "Plain"),('python', "Python"),('html', "HTML"),('sql', "SQL"),('javascript', "Javascript"),('css', "CSS"))
	
	author     = models.ForeignKey(User, related_name='paste_author')
	content    = models.TextField()
	title      = models.CharField(blank=True, max_length=30)
	syntax     = models.CharField(choices=SYNTAX_CHOICES, default='plain', max_length=50)
	createDate = models.DateTimeField(default=datetime.datetime.now, blank=True)
	expiryDate = models.DateTimeField(default=datetime.datetime.now, blank=True)

	class Meta:
		ordering = ('-createDate',)

	def __unicode__(self):
		return "%s" % (self.title or "#%s" % self.id)
	
	@permalink
	def get_absolute_url(self):
		return ('django.views.generic.list.ListView', None, {'object_id': self.id})
	
class PasteAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'title','syntax', 'createDate')
	list_filter  = ('createDate', 'syntax')