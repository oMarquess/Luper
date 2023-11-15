from django.contrib import admin
from django.db.models import Avg, Count, Max
from .models import MovieRating
from celery.schedules import crontab

class MovieRatingAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'last_rating_date', 'rating_count', 'average_rating')
    readonly_fields = ('movie_title', 'last_rating_date', 'rating_count', 'average_rating')

    def get_queryset(self, request):
        # Annotate the queryset with the required aggregated fields
        qs = super().get_queryset(request)
        return qs.annotate(
            _last_rating_date=Max('created_at'),
            _rating_count=Count('id'),
            _average_rating=Avg('overall_rating')
        )

    def movie_title(self, obj):
        return obj.movie.title
    movie_title.admin_order_field = 'movie__title'

    def last_rating_date(self, obj):
        return obj._last_rating_date
    last_rating_date.admin_order_field = '_last_rating_date'

    def rating_count(self, obj):
        return obj._rating_count
    rating_count.admin_order_field = '_rating_count'

    def average_rating(self, obj):
        return obj._average_rating
    average_rating.admin_order_field = '_average_rating'

# Register your models here.
admin.site.register(MovieRating, MovieRatingAdmin)


CELERY_BEAT_SCHEDULE = {
    'calculate-average-rating-everyday': {
        'task': 'Luper.tasks.run_calculate_average_rating',
        'schedule': crontab(hour=12, minute=00),  # Runs every day at midnight
    },
}
