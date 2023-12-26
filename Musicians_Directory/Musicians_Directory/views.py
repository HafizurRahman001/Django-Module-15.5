from django.shortcuts import render
from Album.models import AddAlbum


def home(request):
    display_data = AddAlbum.objects.all()
    return render(request,'display_data.html', {'allData':display_data})