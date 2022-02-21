from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import MovieForm
def demo(request):
    Movie=movie.objects.all()
    context={
        'movie_list':Movie
    }
    return render(request,'index.html',context)

def detail(request,mvid):
    Movie=movie.objects.get(id=mvid)
    return render(request,"detail.html",{'Movie':Movie})


def add_movie(requet):
    if requet.method=="POST":
        name=requet.POST.get('name',)
        desc = requet.POST.get('desc', )
        year =  requet.POST.get('year', )
        img = requet.FILES['img']
        Movie=movie(name=name,desc=desc,year=year,img=img)
        Movie.save()

    return render(requet,'add.html')


def update(request,id):
    Movie=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES, instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'Movie':Movie})

def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')


# Create your views here.
