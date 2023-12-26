from django.shortcuts import render,redirect
from musician.forms  import AddMusicianForm
from musician.models import AddMusician

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musician_form = AddMusicianForm(request.POST)
        if musician_form.is_valid():
            print(musician_form)
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = AddMusicianForm()
    return render(request,'musicianform.html',{'form':musician_form})



def edit_musician(request,id):
    post = AddMusician.objects.get(pk=id)
    musician_form = AddMusicianForm(instance=post)
    if request.method == 'POST':
        musician_form = AddMusicianForm(request.POST,instance=post)
        if musician_form.is_valid():
            print(musician_form)
            musician_form.save()
            return redirect('home')
    return render(request,'musicianform.html',{'form':musician_form})
