from django.shortcuts import render, redirect
from .views import *
from Account.models import *
from Account.views import *
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def isuser(id):
    try:
        user = UserTable.objects.get(id=id)
        return True
    except UserTable.DoesNotExist:
        return redirect('signup')

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

def userdashboard(request):
    try:
        user_id = request.session['id']
        if isuser(user_id):
            user = UserTable.objects.get(id=user_id)
            tasks = TaskTable.objects.filter(user=user).order_by('-date')  # order latest first

            # Pagination (3 per page)
            paginator = Paginator(tasks, 3)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'userdashboard.html', {
                'user': user,
                'number_of_task': tasks.count(),
                'task': page_obj,   # pass page_obj instead of task
            })
        else:
            return redirect('signup')
    except KeyError:
        return redirect('signup')

    
def admindashboard(request):
    try:
        admin_id = request.session['admin_id']
        if isuser(admin_id):
            user = AdminTable.objects.get(admin_id=admin_id)
            tasks = TaskTable.objects.all()
            return render(request, 'admindashboard.html', {'user':user, 'number_of_task':len(tasks),  'task':tasks})
        else:
            return redirect('signup')
    except KeyError:
        return redirect('signup')


def task(request):
    try:
        user_id = request.session['id']
        if isuser(user_id):
            if request.method == 'POST':
                action = request.POST['action']
                if action == 'add':
                    date = request.POST['date']
                    description = request.POST['description']
                    location = request.POST['location']
                    status = request.POST['status']
                    title = request.POST['title']
                    user = UserTable.objects.get(id=user_id)
                    new = TaskTable(date=date, description=description, loction=location, status=status, title=title, user=user )
                    new.save()
                    return redirect('userdashboard')
                elif action == 'edit':
                    task_id = request.POST['task_id']
                    date = request.POST['date']
                    description = request.POST['description']
                    location = request.POST['location']
                    status = request.POST['status']
                    title = request.POST['title']
                    task_edit = TaskTable.objects.get(id=task_id)
                    task_edit.title = title
                    task_edit.description = description
                    task_edit.loction = location
                    task_edit.status=status
                    task_edit.date = date
                    task_edit.save()
                    return redirect('userdashboard')
                elif action=='del':
                    task_id = request.POST['task_id']
                    task_del = TaskTable.objects.get(id=task_id)
                    task_del.delete()
                    return redirect('userdashboard')
            return redirect('userdashboard')
    except KeyError:
        return redirect('signup')

def adminsearch(request):
    if request.method == 'POST':
        startDate = request.POST.get('startDate')
        searchTitle = request.POST.get('searchTitle')
        searchstatus = request.POST.get('searchstatus')

        events = TaskTable.objects.all()

        admin_id = request.session['admin_id']
        user = AdminTable.objects.get(admin_id=admin_id)
        

        # Apply filters
        if searchTitle:
            events = events.filter(title__icontains=searchTitle)  # case-insensitive search
        elif startDate:
            events = events.filter(date__gte=startDate)
        elif searchstatus:
            events = events.filter(status=searchstatus)
        else:
            return render(request, 'admindashboard.html', {'user':user, 'number_of_task':len(events),  'task':events})
        
        return render(request, 'admindashboard.html', {'user':user, 'number_of_task':len(events),  'task':events})

    return redirect('admindashboard')

def search(request):
    if request.method == 'POST':
        startDate = request.POST.get('startDate')
        searchTitle = request.POST.get('searchTitle')
        searchstatus = request.POST.get('searchstatus')

        id = request.session['id']
        user = UserTable.objects.get(id=id)

        events = TaskTable.objects.filter(user=user)

        # Apply filters
        if searchTitle:
            events = events.filter(title__icontains=searchTitle)  # case-insensitive search
        elif startDate:
            events = events.filter(date__gte=startDate)
        elif searchstatus:
            events = events.filter(status=searchstatus)
        else:
            return render(request, 'userdashboard.html', {'user':user, 'number_of_task':len(events),  'task':events})
        return render(request, 'userdashboard.html', {'user':user, 'number_of_task':len(events),  'task':events})

    return redirect('userdashboard')

def newpassword(request):
    if request.method == 'POST':
        action = request.POST['action']
        id = request.POST['id']
        if action == 'admin':
            user = AdminTable.objects.get(admin_id=id)
        else:
            user = UserTable.objects.get(id=id)
        oldpwd = request.POST['oldpwd']
        newpwd = request.POST['newpwd']

        # Check old password
        if user.password == oldpwd:  
            user.password = newpwd
            user.save()
            request.session.clear()

            messages.success(request, "Password changed successfully! Please login again.")
            if action=='admin':
                return redirect('adminlogin')
            else:
                return redirect('login')

        else:
            messages.error(request, "Password does not match. Try again.")
            if action=='admin':
                return redirect('admindashboard')
            else:
                return redirect('task')

def admineditstatus(request):
    if request.method == 'POST':
        id = request.POST['id']
        status = request.POST['status']
        event = TaskTable.objects.get(id=id)
        event.status = status
        event.save()
        return redirect('admindashboard')