from django.shortcuts import render,redirect
from django.views import View

from django.contrib import messages
from chat.models import ChatRoom

APPLICATION = "chat/rooms"

class HomeView(View):
    view_name = 'home'
    template = f'{APPLICATION}/{view_name}.html'

    def get(self,request,*args,**kwargs):
        print(request.user.user_permission)
        if request.user.is_superuser:
            rooms = ChatRoom.objects.all()
        else:
            user_room = request.user.chat_room
            print(user_room)
            rooms=ChatRoom.objects.get(reference=user_room)
        context = {
            'rooms':rooms
        }
        return render(request,self.template,context)