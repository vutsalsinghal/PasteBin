from django.contrib import admin
from pastebin.models import Paste, PasteAdmin

admin.site.register(Paste,PasteAdmin)
