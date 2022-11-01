from django.contrib import admin


# Registered models.

from .models import Venue
from .models import Volunteer
from .models import Event



admin.site.register(Volunteer)



@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_name', 'address', 'web_link', 'phone', 'email')
    ordering = ('venue_name',)
    search_fields = ('venue_name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('event_name', 'venue'), "event_date", "description", "organizer","volunteers")
    list_display = ('event_name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)