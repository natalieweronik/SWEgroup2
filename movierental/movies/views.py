from django.http import HttpResponse
from django.template import loader
from .models import Movie_Table, User_Table
from django.shortcuts import render
from django.db.models import Q

def login(request):
    return render(request,'login.html')
def sign_up(request):
    return render(request, 'signup.html')
def authenticate(request):
    email = request.GET.get('e')
    password = request.GET.get('p')
    if (email!=None) & (password!=None):
        try:
            result = User_Table.objects.get(Q(email=email) & Q(password=password))
            if email[-12:-3]=='@company.':
                return render(request,'adminHome.html')
            return render(request,'userMovies.html')
        except User_Table.DoesNotExist:
            result='not found'
            context={'result': result}
            return render(request,'login.html',context=context)
    return render(request,'login.html')
def add_user(request):
    email = request.GET.get('e')
    password = request.GET.get('p')
    password_conf = request.GET.get('pc')
    name = request.GET.get('n')
    address = request.GET.get('a')
    phone = request.GET.get('ph')
    if ((password != password_conf)):
        return render(request,'signup.html')
    try:
        result = User_Table.objects.get(Q(email=email))
        return render(request,'signup.html')
    except User_Table.DoesNotExist:
        result = User_Table.objects.create(email=email, password=password,address=address,name=name,phone=phone)
        if email[-12:-3]=='@company.':
            return render(request,'adminHome.html')
        return render(request,'userMovies.html')


def to_usermovie(request):
    return render(request,'userMovies.html')
def to_adminmovie(request):
    return render(request,'adminMovies.html')
def to_adminhome(request):
    return render(request,'adminHome.html')
def to_userhome(request):
    return render(request,'index.html')
def to_usersetting(request):
    return render(request,'userSettings.html')
def to_adminsetting(request):
    return render(request,'adminSettings.html')
def to_userpop(request):
    return render(request,'userPop.html')
def to_usershows(request):
    return render(request,'userShows.html')
def to_userrent(request):
    return render(request,'userRent.html')
def to_adminpop(request):
    return render(request,'adminPop.html')
def to_adminshows(request):
    return render(request,'adminShows.html')
def to_pay(request):
    return render(request,'pay.html')
def to_video(request):
    return render(request,'videoPlayer.html')

def movie_search_input(request):
    return render(request, 'search.html')
def search_movies(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Movie_Table.objects.filter(
            Q(title__icontains=query) |
            Q(genre__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'results.html', context)

def movie_detail(request, movie_id):
    try:
        movie = Movie_Table.objects.get(pk=movie_id)
    except Movie_Table.DoesNotExist:
        # You might want to render a 404 page here
        return render(request, 'details.html', {'movie_id': movie_id})

    context = {
        'movie': movie,
    }
    return render(request, 'details.html', context)
