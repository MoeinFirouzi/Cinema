from django.urls import path

from ticketing import views

app_name = 'ticketing'

urlpatterns = [
    path('movie/list/', views.movie_list, name='movie_list'),
    path('cinema/list/', views.cinema_list, name='cinema_list'),
    path('cinema/details/<int:cinema_id>', views.cinema_details, name='cinema_details'),
    path('movie/details/<int:movie_id>', views.movie_details, name='movie_details'),
    path('showtime/list/', views.showtime_list, name='showtime_list')
    # """
    # read https://docs.djangoproject.com/en/3.0/topics/http/urls/
    # Also we can use RegEx
    # """
]
