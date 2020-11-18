from django.urls import path
from . import views

app_name = 'calendarapp'
urlpatterns = [
    path('/index/', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='calendar'),
    path('todolist/', views.todolist, name='todolist'),
    path('todolist/search/', views.search, name='search'),
    path('event/new/', views.create_event, name='event_new'),
    path('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    path('event/delete/<int:id>/', views.Event_Delete, name='event_delete'),
]