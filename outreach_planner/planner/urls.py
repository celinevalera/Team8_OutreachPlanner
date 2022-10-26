from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venue', views.list_venue, name='list-venue'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('search_venue', views.search_venue, name='search-venue'),
    path('inbox/',views.inbox, name="inbox"),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('add_event', views.add_event, name='add-event'),
    path('list_event', views.list_event, name='list-event'),
    path('show_event/<event_id>', views.show_event, name='show-event'),
    path('search_event', views.search_event, name='search-event'),
    path('update_event/<event_id>', views.update_event, name='update-event'),

    path('calendar/',views.calendar),
]