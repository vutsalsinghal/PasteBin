from django.conf.urls import url, include
from django.contrib import admin
from pastebin.models import Paste
from django.views.generic import TemplateView
from pastebin.views import paste_form, paste_list, paste_detail, logout

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
	url(r'^paste_list$', paste_list.page, name='paste_list'),
	url(r'^paste_detail/(?P<object_id>\d+)/$', paste_detail.page, name='paste_detail'),
	url(r'^paste$', paste_form.page, name='paste_form'),

	# Social Login
	url(r'^login$', TemplateView.as_view(template_name='login.html'), name='login'),
	url(r'^logout$', logout.page, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
]