from django.urls import path

from jokes.api.v1 import views

app_name = 'jokes'
urlpatterns = [
    path(
        'random/',
        views.RandomJokeView.as_view(),
        name='random_joke'
    ),
    path(
        'category/<str:category>/',
        views.RandomCategoryJokeView.as_view(),
        name='random_category_joke'
    ),
    path(
        'filter',
        views.FilteredJokesView.as_view(),
        name='filtered_jokes'
    ),
    path(
        'subscribe/',
        views.SubscribeView.as_view(),
        name='subscribe'
    )
]
