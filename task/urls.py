from django.urls import path
from  . views import *

urlpatterns = [
   
    path("",home),
    path("home/",home),
    path("add-task/",task_add),
    path("delete-task/<int:id>",delete_task),
    path("update-task/<int:id>",update_task),
]
