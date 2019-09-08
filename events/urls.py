from django.urls import path
from events import views


app_name = 'events'
urlpatterns = [
	path('', views.home, name='home'),
	path('now/', views.event_list, name='event-list'),
	path('create/', views.create_event, name='create-event'),
	path('<int:event_id>/', views.event_detail, name='event-detail'),
	path('<int:event_id>/update', views.event_update, name='update-event'),
	path('<int:event_id>/delete', views.event_delete, name='delete-event'),
	path('<int:event_id>/book', views.event_book, name='event-book'),
	path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='signin'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
