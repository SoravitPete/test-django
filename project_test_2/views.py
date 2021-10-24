from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi Pete")

def watch_anime(request):
    return HttpResponse("what anime do you want to watch?")

def search(request, keyword, page):
    return HttpResponse(f'Search for: {keyword} page: {page}')

def redirect(request, url):
    return HttpResponse(f'<a href="{url}" target="_blank"> Click here to redirect</a>')

def date(request, day, month, year):
    return HttpResponse(F'Date: {day} - {month} - {year}')

def show_article(request, id, title):
    return HttpResponse(f'ID: {id} <br>Title: {title}')