from django.shortcuts import render
from .models import Room
# Create your views here.

# rooms = [
#     {'id':1,'name':'Start learning python'},
#     {'id':2,'name':'Start learning UI/UX'},
#     {'id':3,'name':'Start learning React'}
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)
