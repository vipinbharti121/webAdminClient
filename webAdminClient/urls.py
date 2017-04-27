"""webAdminClient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from events import views as eventView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^createEvent/', eventView.create_events),
    url(r'^findEvent', eventView.find_events),
    url(r'^deleteEvent/(?P<event_id>\w{0,50})/$', eventView.delete_event),
    url(r'^createPlacement/', eventView.create_placement),
    url(r'^findPlacement', eventView.find_placement),
    url(r'^deletePlacement/(?P<placement_id>\w{0,50})/$', eventView.delete_placement),
    url(r'^$', eventView.index),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
