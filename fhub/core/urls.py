from django.urls import path, include
from . import views

urlpatterns = [
    #showing landing page by default to know about the website
    path('', views.land_view, name='land'),
    #home page url
    path('home/', views.home_views, name='home'),
    #expenses part handling
    path('expenses/', views.expense_dashboard, name='expense-dashboard'),
    path('expenses/delete/<int:expense_id>/', views.delete_expense, name='delete-expense'),
    #authentication part urls
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name = 'logout'),
    #todo page urls
    path('todo/', views.todo_list, name='todo_list'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
    #notes page urls
    path('notes/', views.notes_dashboard, name='notes-dashboard'),
    path('notes/delete/<int:note_id>/', views.delete_note, name='delete-note'),
    path('notes/pin/<int:note_id>/', views.toggle_pin, name='pin-note'),
    path('notes/favorite/<int:note_id>/', views.toggle_favorite, name='favorite-note'),
    path('edit/<int:note_id>/', views.edit_note_view, name='edit-note'),
    path('update/<int:note_id>/', views.update_note_view, name='update-note'),
    #calendar page urls
    path('calendar/', views.calendar_page, name='calendar_page'),
    path('api/events/', views.get_events, name='get_events'),
    path('api/events/add/', views.add_event, name='add_event'),
    path('api/events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    #inventory page urls
    path('inventory/', views.inventory_dashboard, name='inventory-dashboard'),
    path('editt/<int:item_id>/', views.edit_item, name='item_edit'),
    path('deletee/<int:item_id>/', views.delete_item, name='item_delete'),
]
