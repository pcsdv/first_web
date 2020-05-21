
from django.forms import ModelForm
from entries. models import Entry,PatientD
from dems.models import Hompath


class EntryForm(ModelForm):

	class Meta:
		model = Entry
		fields = ('text',)


class HompathForm(ModelForm):

	class Meta:
		model = Hompath
		fields = ('name','first_word','second_word','third_word','fourth_word','antidote','complement','miasm',)


class PatientDForm(ModelForm):
	
	class Meta:
		model = PatientD
		fields = ('code','name','details','dated',)


