from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
	
	path('uplist/', views.UpcomingList.as_view(), name='up-list'),
	path('orglist/', views.OrganizerList.as_view(), name='org-list'),
	path('userlist/', views.UserList.as_view(), name='user-list'),
	path('create/', views.CreateView.as_view(), name='create-event-api'),
	path('<int:event_id>/update/', views.UpdateView.as_view(), name='update-event-api'),
	path('<int:event_id>/book/', views.BookView.as_view(), name='book-event-api'),
	path('<int:event_id>/attendlist/', views.AttendeesView.as_view(), name='attend-list'),

	]

