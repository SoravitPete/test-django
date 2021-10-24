from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi Pete")

def watch_anime(request):
    return HttpResponse("what anime do you want to watch?")