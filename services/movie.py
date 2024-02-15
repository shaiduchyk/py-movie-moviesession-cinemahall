from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list | None = None,
               actors_ids: list | None = None) -> QuerySet:

    movie_queryset = Movie.objects.all()

    if genres_ids:
        movie_queryset = movie_queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        movie_queryset = movie_queryset.filter(actors__id__in=actors_ids)

    return movie_queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list | None = None,
                 actors_ids: list | None = None) -> Movie:

    created_movie = Movie.objects.create(title=movie_title,
                                         description=movie_description)

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        created_movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        created_movie.actors.set(actors)

    return created_movie