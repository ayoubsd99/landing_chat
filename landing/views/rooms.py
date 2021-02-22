from django.shortcuts import render

from django.views import View
from chat.models import ChatRoom
from users.models import User
APPLICATION = "chat/rooms"

class RoomView(View):
    view_name = 'room'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        room = kwargs.get('room_name')
        if request.user.is_superuser:
            rooms = ChatRoom.objects.all()
        else:
            user_room = request.user.chat_room
            print(user_room)
            rooms=ChatRoom.objects.get(reference=user_room)
        context = {
            'room_name':room,
            'rooms':rooms,
            'members': User.objects.filter(chat_room=ChatRoom.objects.get(room_name=room)),
            'admin':User.objects.get(is_superuser=True)
        }
        return render(request,self.template,context)