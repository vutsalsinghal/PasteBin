import datetime
from django.db import models
from django.db.models import permalink
from django.contrib import admin

class Paste(models.Model):
	SYNTAX_CHOICES = (('plain', "Plain"),('python', "Python"),('html', "HTML"),('sql', "SQL"),('javascript', "Javascript"),('css', "CSS"))
	
	content        = models.TextField()
	title          = models.CharField(blank=True, max_length=30)
	syntax         = models.CharField(choices=SYNTAX_CHOICES, default='plain', max_length=50)
	timestamp      = models.DateTimeField(default=datetime.datetime.now, blank=True)

	class Meta:
		ordering = ('-timestamp',)

	def __unicode__(self):
		return "%s" % (self.title or "#%s" % self.id)
	
	@permalink
	def get_absolute_url(self):
		return ('django.views.generic.list.ListView', None, {'object_id': self.id})
	
class PasteAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'title','syntax', 'timestamp')
	list_filter  = ('timestamp', 'syntax')