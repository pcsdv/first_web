
from django.contrib.auth.decorators import  login_required
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import  views
from entries.models import PatientD 


urlpatterns = [
    path('entries/',views.entries_view,name='entries'),
    path('home/',views.home_view,name='entry-home'),
    path('adds/',views.add_view,name='adds'),

    path('hompath/',views.hompath_view,name='hompath'),
    path('addhompath/',views.add_hompath_view,name='ad-hompath'),

    path('hompathlist/',login_required(views.Hompath_ListView.as_view(template_name='entries/hompalist.html')),name='homp-list'),

    path('hompathlist/<int:id>',login_required(views.Hompath_DetailView.as_view(template_name='entries/hompathdetail.html')),name='homp-detail'),


    path('editp/<int:pk>',views.patient_update,name='edit_p'),

    path('creatept/',login_required(views.CreatePatient.as_view(template_name='entries/create_p.html')),name= 'cr_pt'),

    path('patientdtl/',login_required(views.PatientDtl_ListView.as_view(template_name='entries/patientdtl_list.html')),name='pdtl-list'),

    path('patientdtl/<int:id>',login_required(views.PatientDtl_DetailView.as_view(template_name='entries/patientdtl_detail.html')),name='pdtl-detail'),
]

