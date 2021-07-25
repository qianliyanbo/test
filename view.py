from django.http import HttpResponse

def index(request):
    return HttpResponse('hello')

def index2(request):
    print(1111)
    print(22222)
    print(3333)
    print(11111)
    return HttpResponse('word')

