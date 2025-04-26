from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.land_view, name='land'),
    path('home/', views.home_views, name='home'),
    path('expenses/', views.expense_dashboard, name='expense-dashboard'),
    path('expenses/delete/<int:expense_id>/', views.delete_expense, name='delete-expense'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name = 'logout'),
    path('todo/', views.todo_list, name='todo_list'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
]
