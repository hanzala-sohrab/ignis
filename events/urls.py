from django.urls import path
from .views import event_create_and_list_view, like_unlike_event

app_name = 'events'

urlpatterns = [
    path('', event_create_and_list_view, name='main-event-view'),
    path('liked/', like_unlike_event, name='like-event-view'),
]
