from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.search_movies, name='results'),
    path('search/',views.movie_search_input, name='search'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]