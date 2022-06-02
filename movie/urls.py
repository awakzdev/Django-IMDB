from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory, MovieLanguage, MovieSearch, MovieYear, MovieStatus
from . import views

app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('status/<str:status>', MovieStatus.as_view(), name='movie_status'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('year/<int:year>', MovieYear.as_view(), name='movie_year'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('<slug:slug>/add-comment/', views.add_comment, name='add_comment'),
]

