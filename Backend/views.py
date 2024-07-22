from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from Backend.models import Movie
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.
def index_page(request):
    return render(request,"index.html")

def Add_category(request):
    return render(request,"AddCategory.html")

def savedata_Category(request):
    if request.method == "POST":
        ti = request.POST.get('title')
        des = request.POST.get('description')
        r_dt = request.POST.get('release_date')
        gnr = request.POST.get('genre')
        ln = request.POST.get('length')
        img_cr = request.FILES['img_crd']
        img_cvr = request.FILES['img_cvr']
        vw = request.POST.get('views')

        obj = Movie(Title=ti,description=des,release_date=r_dt,genre=gnr,length=ln,image_card=img_cr,image_cover=img_cvr,movie_views=vw)
        obj.save()
        return redirect(Add_category)
def display_Movie(request):
    data = Movie.objects.all()
    return render(request,"Display.html",{'data':data})

def edit_Movie(request,Movieid):
    data = Movie.objects.get(id=Movieid)
    return render(request,"Edit_MovieCategory.html", {'data':data})

def update_Movie(request,Movieid):
    if request.method == 'POST':
        # Handle form submission
        ti = request.POST.get('title')
        des = request.POST.get('description')
        r_dt = request.POST.get('release_date')

        gnr = request.POST.get('genre')
        ln = request.POST.get('length')
        vw = request.POST.get('views')

        # Handle image file if uploaded
        if 'mv_crd' in request.FILES:
            img_card = request.FILES['mv_crd']
            fs = FileSystemStorage()
            image_card = fs.save(img_card.name, img_card)
        else:
            # If no new image uploaded, retain existing image card
            image_card = Movie.objects.get(id=Movieid).image_card

        if 'mv_cvr' in request.FILES:
            img_cover = request.FILES['mv_cvr']
            fs = FileSystemStorage()
            image_cover = fs.save(img_cover.name, img_cover)
        else:
            # If no new image uploaded, retain existing image cover
            image_cover = Movie.objects.get(id=Movieid).image_cover

        # Update movie details
        Movie.objects.filter(id=Movieid).update(Title=ti,description=des,release_date=r_dt,genre=gnr,
        length=ln,image_card=image_card,image_cover=image_cover,movie_views=vw)

        # Add success message
        messages.success(request, 'Movie updated successfully!')
        return redirect('display_Movie')

def delete_Movie(request, Movieid):
    x = Movie.objects.filter(id=Movieid)
    x.delete()
    return redirect(display_Movie)
        # *********************************************************
def login_page(request):
    return render(request,"Login.html")

def login_admin(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)

            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(index_page)

            else:
                return redirect(login_page)
        else:
            return redirect(login_page)

def Adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)
