from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import Student
from django.contrib import messages

# Create your views here.
# Functon view for index index.html
# def index(request):
#     data = Student.objects.all()
#     context = {"data":data}
#     return render(request, 'index.html', context)

#Class View for index
class index(View):
    def get(self, request):
        data = Student.objects.all()
        context = {"data":data}
        return render(request, 'index.html', context)
    

# Funtion Based view for insertData
# def insertData(request):

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         print(name, email, age, gender)
#         query=Student(name=name, email=email, age=age, gender=gender)
#         query.save()
#         messages.info(request, "Data Inserted Sucessfully")
#         return redirect("/")
#     return render(request, 'index.html',)

# Class Based View for insertData
class insertData(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name, email, age, gender)
        query=Student(name=name, email=email, age=age, gender=gender)
        query.save()
        messages.info(request, "Data Inserted Sucessfully")
        return redirect("/")
    

# Function Based View for updateData
# def updateData(request, id):

#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         age = request.POST['age']
#         gender = request.POST['gender']

#         edit=Student.objects.get(id=id)
#         edit.name=name
#         edit.email=email
#         edit.age=age
#         edit.gender=gender
#         edit.save()
#         messages.warning(request, "Data Updated Sucessfully")
#         return redirect("/")
    
#     d = Student.objects.get(id=id)
#     context = {"d":d}
#     return render(request, 'edit.html', context)

#Class Based View for updateData
class updateData(View):
    def get(self, request, id):
        d = Student.objects.get(id=id)
        context = {"d":d}
        return render(request, 'edit.html', context)

    def post(self, request, id):
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.warning(request, "Data Updated Sucessfully")
        return redirect("/")


# Function Based View for deleteData 
# def deleteData(request, id):
#     d = Student.objects.get(id=id)
#     d.delete()
#     messages.error(request, "Data Deleted Sucessfully")
#     return redirect("/")

# Class Based View for deleteData
class deleteData(View):
    def get(self, request, id):
        d = Student.objects.get(id=id)
        d.delete()
        messages.error(request, "Data Deleted Sucessfully")
        return redirect("/")
    
def about(request):
    return render(request, 'about.html')

