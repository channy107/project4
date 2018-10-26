from django.http import HttpResponse
from .models import *
def insert(request):
    for i in range(1, 1001): # 게시물 1000개 입력
        Board.objects.create(title='제목 ' + str(i), content='내용 ' + str(i))
    return HttpResponse('insert 1000')