from django.urls import path
from . import views

urlpatterns = [
   	path('', views.inbox, name='inbox'),
   	path('message/<username>', views.directs, name='directs'),
   	path('new/', views.user_search, name='usersearch'),
   	path('new/<username>', views.new_conversation, name='newconversation'),
   	path('send/', views.senddirect, name='send_direct'),
]