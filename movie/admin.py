from django.contrib import admin
from .models import Movie, MovieLink, Comment


admin.site.register(Movie)
admin.site.register(MovieLink)
admin.site.register(Comment)
