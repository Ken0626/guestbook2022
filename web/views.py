from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from .models import Message
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class MessageList(ListView):
    model = Message
    odering = ['-id']  #值越大越前面

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    fields = ['user',"subject",'content']
    success_url = reverse_lazy('msg_list')

class MessageDelete(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')


    
