
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 


urlpatterns = [
	path('register/',views.register, name='register'),
	#-------
	path('',views.index, name='index'),
	path('logout/',views.logout_view, name='logout'),

	#	path('login/',views.login_view, name='login'),
	#path('register/',views.register_view, name='act-register'),
]
