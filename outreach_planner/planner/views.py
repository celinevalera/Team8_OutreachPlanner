from concurrent.futures import thread
from email.message import Message
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views import View
from django.db.models import Q
from django.views.decorators.cache import cache_control
from .models import Event, MessageModel, ThreadModel,Venue
from .forms import MessageForm, VenueForm, ThreadForm


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
class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        context = {
            'threads': threads
        }
        return render(request, 'inbox.html', context)
class CreateThread(View):
    def get(self, request, *args,**kwargs):
        form =ThreadForm()
        context={
            'form':form
        }
        return render(request, 'create_msg.html', context)

    def post(self, request, *args,**kwargs):
        form = ThreadForm(request.POST)
        username = request.POST.get('username')
        try: 
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user,receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread',pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver,receiver = request.user ).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread',pk=thread.pk)
            if form.is_valid():
                thread = ThreadModel(
                user=request.user,
                receiver=receiver
                )
                thread.save()
                return redirect('thread', pk=thread.pk)
                
        except:            
            return redirect('create-msg')

class InboxView(View):
    def get(self, request,pk, *args,**kwargs):
        form = MessageForm()
        thread =ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread_pk_contains=pk)
        context={
            'thread':thread,
            'form':form,
            'message_list':message_list
        }
        return render(request, 'thread.html', context)

class CreateMessage(View):
    def post(self, request, pk,*args,**kwargs):
        thread=ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else: 
            receiver = thread.receiver
        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message')
        )
        message.save()
        return redirect('thread',pk=pk)


