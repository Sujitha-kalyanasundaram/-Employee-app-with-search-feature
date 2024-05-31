from django.shortcuts import render, redirect, HttpResponse
from empapp.models import Employee  # Correct model class

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        addr = request.POST['addr']

        if not fname or not lname or not age or not addr:
            context['msg'] = "Fields cannot be empty"
        else:
            c = Employee.objects.create(fname=fname, lname=lname, age=age, address=addr)
            c.save()
            context['msg'] = "Employee Added"
    
    return render(request, 'index.html', context)

def display(request):
    context = {}
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        addr = request.POST['addr']

        if not fname or not lname or not age or not addr:
            context['msg'] = "Fields cannot be empty"
        else:
            c = Employee.objects.create(fname=fname, lname=lname, age=age, address=addr)
            c.save()
            context['msg'] = "Employee Added"
        
        d = Employee.objects.all()
        context['data'] = d
    else:
        c = Employee.objects.all()
        context['data'] = c
    
    return render(request, 'index.html', context)

def search(request):
    cat = request.POST.get('category', '')
    opt = request.POST.get('options', '')
    string = request.POST.get('search_string', '')

    if not string:
        string = "error"
    
    url = f"empapp/{cat}/{opt}/{string}"
    print(url)
    return redirect(url)

def look(request, cid, oid, txt):
    context = {}
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        addr = request.POST['addr']

        if not fname or not lname or not age or not addr:
            context['msg'] = "Fields cannot be empty"
        else:
            c = Employee.objects.create(fname=fname, lname=lname, age=age, address=addr)
            c.save()
            context['msg'] = "Employee Added"
            d = Employee.objects.all()
            context['data'] = d
            return render(request, 'index.html', context)
    
    if cid == "empname":
        c = Employee.objects.all()
        context['data'] = []

        if oid == "startswith":
            for x in c:
                if x.fname.lower().startswith(txt.lower()):
                    context['data'].append(x)
            if not context['data']:
                context['errmsg'] = "No Data found"

        elif oid == "contains":
            for x in c:
                if txt.lower() in x.fname.lower() or txt.lower() in x.lname.lower():
                    context['data'].append(x)
            if not context['data']:
                context['errmsg'] = "No Data found"

        else:
            context['error'] = "Invalid lookup option! Please choose startswith or contains option"
    
    elif cid == "age" and oid == "lte":
        try:
            ag = int(txt)
            c = Employee.objects.filter(age__lte=ag)
            context['data'] = c
            if not context['data']:
                context['errmsg'] = "No Data found"
        except ValueError:
            context['error'] = "Invalid age format"
    
    else:
        context['error'] = "Invalid lookup option! Please choose age less than option"
    
    return render(request, 'index.html', context)
