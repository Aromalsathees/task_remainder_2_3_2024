from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add_task',views.add_task,name='add_task'),
    path('delete_task/<id>',views.delete_task,name='delete_task'),
#   path('update_task/<id>',views.update_task,name='update_task')
    path('mark_as_done/<id>',views.mark_as_done,name='mark_as_done'),
    path('mark_as_undone/<id>',views.mark_as_undone,name='mark_as_undone'),
    
]
