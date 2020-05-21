
from django.template import loader
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from django.contrib.auth.decorators import  login_required
from django.http import HttpResponseRedirect,HttpResponse
from entries.models import Entry,PatientD
from entries.forms import EntryForm,HompathForm,PatientDForm 
from django.views.generic.edit import FormView
from dems.models import Hompath,BioChemic



@login_required(login_url="/login/")
def home_view(request,template='entries/home.html'):
	return render(request,template)


@login_required(login_url="/login/")
def entries_view(request):
	obj = Entry.objects.all()
	context = {
			'over' : obj
			}
	return render(request,'entries/entries.html',context)


@login_required(login_url="/login/")
def add_view(request):
	if request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/entries/home/')
	else:
		form = EntryForm()
	context = {'form':form }
	return render(request,'entries/adds.html',context)





@login_required(login_url="/login/")
def hompath_view(request,template='entries/hompath.html'):
	obj = Hompath.objects.all()
	context = { 'over' : obj }

	return render(request, template, context)

@login_required(login_url="/login/")
def add_hompath_view(request):
	if request.method == "POST":
		form = HompathForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/entries/hompath/')
	else:
		form = HompathForm()
		context = {'form':form }
	return render(request,'entries/add_hompath.html',context)

class Hompath_ListView(ListView):
	model = Hompath
	context_object_name = 'hom'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['hoho'] = Hompath.objects.all()
		return context

class Hompath_DetailView(DetailView):
	model = Hompath
	context_object_name = 'ho'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Hompath,id=id_)

class PatientDtl_ListView(ListView):
	model = PatientD
	context_object_name = 'fofo'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['momo'] = PatientD.objects.all()
		return context

class PatientDtl_DetailView(DetailView):
	model = PatientD
	context_object_name = 'doc'
	
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(PatientD,id=id_)

class CreatePatient(FormView):
	model = PatientD
	form_class = PatientDForm
	success_url ="/entries/home/"
	template_name = "entries/create_p.html"

	def form_valid(self, form):
		form.save()
		return super(CreatePatient, self).form_valid(form)

def patient_update(request, pk, template_name='entries/create_p.html'):
	book= get_object_or_404(PatientD, pk=pk)
	form = PatientDForm(request.POST or None, instance=book)
	if form.is_valid():
		form.save()
		return redirect('cr_pt')
	return render(request, template_name, {'form':form})



