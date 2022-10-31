from django.contrib import admin


# Registered models.

from .models import Venue
from .models import Volunteer
from .models import Event

from .models import ThreadModel
from .models import MessageModel

admin.site.register(Volunteer)
admin.site.register(ThreadModel)
admin.site.register(MessageModel)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_name', 'address', 'web_link', 'phone', 'email')
    ordering = ('venue_name',)
    search_fields = ('venue_name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('event_name', 'venue'), "event_date", "description", "organizer")
    list_display = ('event_name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)