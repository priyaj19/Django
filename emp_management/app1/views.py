from django.shortcuts import render,redirect
from .models import Employee,Departments

# Create your views here.

def index(request):
   
    data = Employee.objects.all()
    return render(request,"index.html",{'employees':data})

def addemp(request):
    try:
        dpts = Departments.objects.all()
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            gender = request.POST['gender']
            department = request.POST['department']
            salary = request.POST['salary']
            image = request.FILES.get('image')
            department = Departments.objects.get(name=department)
            data = Employee.objects.create(name=name,email=email,contact=contact,gender=gender,salary=salary,image=image,department=department)
            return redirect('index')
    except:
        error = "there is something went wrong"
        return render(request,"addemp.html",{'dpts':dpts,"error":error})
    
    return render(request,"addemp.html",{'dpts':dpts})


def emp_dlt(request,eid):
    data = Employee.objects.get(id=eid)
    data.delete()
    return redirect("index")



def emp_updt(request,eid):
    data = Employee.objects.get(id=eid)
    dpts = Departments.objects.all()
    if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            gender = request.POST['gender']
            department = request.POST['department']
            salary = request.POST['salary']
            image = request.FILES.get('image')
            department = Departments.objects.get(name=department)
            data = Employee(id=eid,name=name,email=email,contact=contact,gender=gender,salary=salary,image=image,department=department)
            data.save()
            return render(request,"view.html",{'employee':data})
    return render(request,"update.html",{'employee':data,'dpts':dpts})


def emp_view(request,eid):
    data = Employee.objects.get(id=eid)
    return render(request,"view.html",{'employee':data})


    
def search_data(request):
    var = request.GET.get('search')
    data = Employee.objects.filter(email__iexact=var)
    return render(request,"index.html",{'employees':data})


def search_male(request):
    data = Employee.objects.filter(gender__iexact="male")
    return render(request,"index.html",{'employees':data})


def search_female(request):
    data = Employee.objects.filter(gender__iexact="female")
    return render(request,"index.html",{'employees':data})

def asc_salary(request):
    data = Employee.objects.all().order_by('salary')
    return render(request,"index.html",{'employees':data})

def desc_salary(request):
    data = Employee.objects.all().order_by('-salary')
    return render(request,"index.html",{'employees':data})


def search_dpt(request):
    
    dpt = request.GET.get('dpt')
    department = Departments.objects.get(name = dpt)
    data = Employee.objects.filter(department=department)
    return render(request,"index.html",{'employees':data})