from django.contrib import admin
from .models import Movie, MovieLink, Comment


admin.site.register(Movie)
admin.site.register(MovieLink)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on', )
    search_fields = ('name', 'body')

