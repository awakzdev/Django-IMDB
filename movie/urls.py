from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory, MovieLanguage, MovieSearch, MovieYear
from . import views

app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('year/<int:year>', MovieYear.as_view(), name='movie_year'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('<slug:slug>/add-comment/', views.add_comment, name='add-comment'),
    path('<slug:slug>/create/', views.comment_create, name='create-comment'),
]

