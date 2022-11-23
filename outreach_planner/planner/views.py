from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import cache_control
from .models import Event,Venue
from .forms import VenueForm,EventForm
from django.views.decorators.csrf import csrf_exempt


from xhtml2pdf import pisa
from django.template.loader import get_template


@login_required(login_url='/users/login_user')
def home(request):
    event_list = Event.objects.all().order_by('event_date')
    return render(request, 'dashboard.html',
    {'event_list': event_list})

#Venue
@staff_member_required(login_url='home')
def add_venue(request):
    submitted = False
    
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Venues/add_venue.html', {'form': form, 'submitted': submitted})

def list_venue(request):
    venue_list = Venue.objects.all().order_by('venue_name')
    return render(request, 'Venues/venue.html',
    {'venue_list': venue_list})

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'Venues/show_venue.html',
    {'venue': venue})

def search_venue(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(venue_name__contains=searched)
        return render(request, 'Venues/search_venue.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'Venues/search_venue.html', {})

@staff_member_required(login_url='home')
def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, request.FILES or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('show-venue', venue.id)
    return render(request, 'Venues/update_venue.html',
    {'venue': venue, 'form': form})

@staff_member_required(login_url='home')
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venue')



def calendar(request):
    event_list = Event.objects.all()
    return render(request, 'calendar.html',
    {'event_list': event_list})


#Event
@staff_member_required(login_url='home')
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Events/add_event.html', {'form': form, 'submitted': submitted})

def list_event(request):
    event_list = Event.objects.all().order_by('event_name')
    return render(request, 'Events/event.html',
    {'event_list': event_list})

def show_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'Events/show_event.html',
    {'event': event})

def search_event(request):
    if request.method == "POST":
        searched = request.POST['searched']
        event = Event.objects.filter(event_name__contains=searched)
        return render(request, 'Events/search_event.html', {'searched':searched, 'event':event})
    else:
        return render(request, 'Events/search_event.html', {})

@staff_member_required(login_url='home')
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if form.is_valid():
        form.save(commit=False)
        form.save()
        return redirect('show-event', event.id)
    return render(request, 'Events/update_event.html',
    {'event': event, 'form': form})

@staff_member_required(login_url='home')
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-event')


#newly added
@login_required(login_url='/login')
def registration_confirmation(request,event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == "POST":
        event.volunteers.add(request.user)
        return redirect('list-event')
    return render(request, 'Events/registration_confirmation.html',{'event':event})



#   Generate PDF File Event Summary
def event_pdf(request, event_id):
    event = Event.objects.get(pk=event_id)

    template_path = 'Events/pdfSummary.html'
    context = {'event': event}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="event-summary.pdf"'
    template = get_template(template_path)
    html = template.render(context)


    pisa_status = pisa.CreatePDF(
       html, dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response