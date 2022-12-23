from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Message
from django.urls import reverse_lazy


class MessageList(ListView):
    model = Message
    odering = ['-id']  #值越大越前面

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    fields = ['user',"subject",'content']
    success_url = reverse_lazy('msg_list')


