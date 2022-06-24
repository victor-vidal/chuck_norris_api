from django.urls import path

from jokes.api.v1 import views

app_name = 'jokes'
urlpatterns = [
    path(
        'random/',
        views.random_joke,
        name='random_joke'
    )
]
