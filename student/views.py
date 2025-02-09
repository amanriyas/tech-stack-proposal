from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework import status
# Create your views here.

class Index(APIView):

    def get(self,request):
        return Response({"message": "Hello from Django!"})
 
class GetStudent(APIView):
    def get(self,request):
        students = Student.objects.all()
        student_serializer = StudentSerializer(students, many = True)
        return Response(student_serializer.data, status=200)
    
class DeleteStudent(APIView):
    def delete(self, request,pk):
        Student.objects.filter(pk=pk).delete()

        return Response({"message": "Role deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
      
class AddStudent(APIView):
       def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save() # the data sent is added to the database
            response_data = {
                "message": "Role added successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class UpdateStudent(APIView):
     def get_object(self, pk):
        return get_object_or_404(Student, pk=pk)

     def put(self, request, pk):
        role = self.get_object(pk)
        serializer = StudentSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Role updated successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
     
class OneStudent(APIView):
    def get(self, request,pk):
        student = Student.objects.filter(pk = pk)
        student_serializer = StudentSerializer(student, many = True) 
        return Response(student_serializer.data, status=200)    
              
          