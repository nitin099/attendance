"""attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tit.views import create ,saved , attended,calculate,retrive,home, updatedays,updatestudent,detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create/',create,name='create' ),
    url(r'^home/',home , name='home'),
    url(r'^saved/',saved, name='saved' ),
    url(r'^attended/',attended, name='attended' ),
    url(r'^calculate/(?P<id>\d+)',calculate, name="calculate" ),
    url(r'^updatestudent/(?P<id>\d+)',updatestudent, name="updatestudent" ),
    url(r'^updatedays/',updatedays, name="updatedays" ),
    url(r'^retrive/',retrive, name='retrive' ),
    url(r'^detail/(?P<id>\d+)',detail, name='detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIAL_URL , document_root = settings.MEDIA_ROOT)
