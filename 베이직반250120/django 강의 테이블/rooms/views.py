from django.shortcuts import render
from .models import Room

def room_list(request):
    # 강의 ID 순으로 정렬
    rooms = Room.objects.all().order_by('lecture_id') # 모든 강의 목록을 가져오고 강의 ID 순으로 정렬   
    return render(request, 'rooms/room_list.html', {'rooms': rooms}) # 강의 목록 페이지 렌더링