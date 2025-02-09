from django.urls import path
from student.views import *


urlpatterns = [
    path('',Index.as_view(), name = "index"),
    path('get-students/',GetStudent.as_view(), name = "get-students"),
    path('delete-student/<int:pk>/',DeleteStudent.as_view(), name = "delete-student"),
    path('add-student/',AddStudent.as_view(), name = "add-student"),
    path('update-student/<int:pk>/',UpdateStudent.as_view(), name = "update-student"),
    path('get-one-student/<int:pk>/',OneStudent.as_view(), name = "gets-one-student"),
    
]