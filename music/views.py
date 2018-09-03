from django.http import HttpResponse
from .models import Albums
from django.http import Http404


def index(request):
    all_albums = Albums.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)


def detail(request,album_id):
    try:
        album=Albums.get(pk=album_id)
    except Albums.DoesNotExist:
        raise Http404("Album doesnot exist")
