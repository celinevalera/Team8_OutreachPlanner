from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Event, Inbox
from .models import Event, Venue
from .forms import VenueForm

@login_required(login_url='/users/login_user')
def home(request):
    event_list = Event.objects.all().order_by('event_date')
    return render(request, 'dashboard.html', 
    {'event_list': event_list})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else: 
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_venue.html', {'form': form, 'submitted': submitted})

def list_venue(request):
    venue_list = Venue.objects.all().order_by('venue_name')
    return render(request, 'venue.html', 
    {'venue_list': venue_list})

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'show_venue.html', 
    {'venue': venue})

def search_venue(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(venue_name__contains=searched)
        return render(request, 'search_venue.html', {'searched': searched, 'venues': venues})
    else: 
        return render(request, 'search_venue.html', {})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('show-venue', venue.id)
    return render(request, 'update_venue.html', 
    {'venue': venue, 'form': form})

def calendar(request):
    event_list = Event.objects.all()
    return render(request, 'calendar.html',
    {'event_list': event_list})

#Inbox
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True)
def inbox(request):
    email_list = Inbox.objects.all()
    return render(request, 'inbox.html',{'email_list':email_list})

def show_msg(request,inbox_id):
    email = Inbox.objects.get(pk=inbox_id)
    return render(request, 'show_msg.html',{'email':email})

def create_msg(request):
    return render(request, 'create_msg.html', {})