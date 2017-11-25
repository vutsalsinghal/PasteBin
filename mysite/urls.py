from django.conf.urls import url
from django.contrib import admin
from pastebin.models import Paste
from django.views.generic import TemplateView
from pastebin.views import paste_form, paste_list, paste_detail

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
	url(r'^paste_list$', paste_list.page, name='paste_list'),           # allow_empty=True),
	url(r'^(?P<object_id>\d+)/$', paste_detail.page, name='paste_detail'),
	url(r'^paste$', paste_form.page, name='paste_form'),
]