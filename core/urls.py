from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from journal.views import page404,index

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('journal/',include("journal.urls"))
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r"^.*$",page404)]