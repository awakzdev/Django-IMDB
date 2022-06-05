from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie, MovieLink
from .forms import CommentForm
from . import forms


class HomeView(ListView):
    model = Movie
    template_name = 'movie/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['recently_added'] = Movie.objects.filter(status='RA')
        return context


class MovieList(ListView):
    model = Movie
    paginate_by = 5


class MovieDetail(DetailView):
    model = Movie

    def render_to_response(self, *args, **kwargs):
        self.object.refresh_from_db()
        self.object.views_count += 1
        self.object.save()
        return super().render_to_response(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = MovieLink.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)
        return context


class MovieStatus(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        self.status = self.kwargs['status']
        return Movie.objects.filter(status=self.status)

    def get_context_data(self, **kwargs):
        context = super(MovieStatus, self).get_context_data(**kwargs)
        context['movie_status'] = self.status
        return context


class MovieCategory(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context


class MovieLanguage(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context


class MovieSearch(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)

        else:
            object_list = self.model.objects.none()
        return object_list


class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True
    paginate_by = 5


@login_required(login_url='/accounts/login/')
def comment_create(request, slug):
    movie = Movie.objects.get(slug=slug)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST, request.FILES)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = movie
            comment.author = request.user
            form.save()
            return redirect('movies:movie_detail', slug=slug)
    else:
        form = forms.CommentForm()
    return render(request, 'movie/add_comment.html', {'form': form})
