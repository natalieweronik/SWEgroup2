from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.search_movies, name='results'),
    path('search/',views.movie_search_input, name='search'),
    path('results/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('sign-up',views.sign_up, name="sign_up"),
    path('login',views.login, name='log_in'),
    path('movies/',views.authenticate, name='auth'),
    path('new/movies/',views.add_user, name='add'),
    path('user/movies/',views.to_usermovie, name='usermovies'),
    path('pay/',views.to_pay, name='pay'),
    path('watch/',views.to_video, name='watch'),
    path('admin/movies/',views.to_adminmovie, name='adminmovies'),
    path('admin/home/',views.to_adminhome, name='adminhome'),
    path('user/home/',views.to_userhome, name='userhome'),
    path('user/settings/',views.to_usersetting, name='userset'),
    path('admin/setting/',views.to_adminsetting, name='adminset'),
    path('user/popular/',views.to_userpop, name='userpop'),
    path('user/shows/',views.to_usershows, name='usershow'),
    path('user/rentals/',views.to_userrent, name='userrent'),
    path('admin/popular/',views.to_adminpop, name='adminpop'),
    path('admin/shows/',views.to_adminshows, name='adminshow'),
    path('add-user',views.add_user, name='add_user'),
]