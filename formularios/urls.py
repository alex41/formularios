"""formularios URL Configuration

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


from formulario.views import RegistroCreate 
from formulario.views import RegistroList
from django.conf.urls import url, include 
from django.conf import settings #se trae los settings
from django.conf.urls.static import static # se trae los static 

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', RegistroList.as_view(), name='list'),
    url(r'eventos/', RegistroCreate.as_view(), name='crear'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # se configura los static 


