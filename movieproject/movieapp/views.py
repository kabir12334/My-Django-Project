from django.shortcuts import render
from movieapp.forms import MovieForm
from movieapp.models import Movie
# Create your views here.

def index(request):
    return render(request,'html/index.html')

def add_movie_view(request):
    form=MovieForm()
    if request.method =='POST':
        form =MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'html/addmovie.html',{'form':form})

def list_movie_view(request):
    movie_list= Movie.objects.all().order_by('-rating')
    return render(request,'html/listmovie.html',{'movie_list':movie_list})