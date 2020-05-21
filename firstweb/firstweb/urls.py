
from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
#from django.urls import reverse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dems/',include('dems.urls')),
    path('entries/',include('entries.urls')),
    path('',include('action.urls')),
    path('accounts',include('django.contrib.auth.urls')),
]

if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
