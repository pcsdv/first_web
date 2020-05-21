from django.contrib import admin

from entries.models import Entry,PatientD


class EntryAdmin(admin.ModelAdmin):
	list_display=['date_posted']
	search_fields = ['date_posted']
admin.site.register(Entry,EntryAdmin)

class PatientDAdmin(admin.ModelAdmin):
	list_display=['name','code']
	search_fields = ['name']
admin.site.register(PatientD,PatientDAdmin)
