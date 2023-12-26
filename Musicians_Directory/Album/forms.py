from django import forms 
from Album.models import AddAlbum


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = AddAlbum
        fields = '__all__'

        widgets={
            'album_reels_date':forms.DateInput(attrs={'type':'date'})
        }