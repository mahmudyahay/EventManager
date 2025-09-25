from django.shortcuts import render, redirect
from .views import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings
import random
from TaskModule.views import *

# Create your views here.

# to send emails
def send_email(mail, message, subject):
    subject = subject
    message = message
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [mail]

    send_mail(subject, message, from_email, recipient_list)

# for admin validation
def isadmin(id):
    try:
        admin = AdminTable.objects.get(id=id)
        if admin.role == 'admin':
            return True
        else:
            return False
    except KeyError:
        return False

# login admin if details are correct redirect to admindashboard and if admin is already login, redirect to admindashboard
def adminlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = AdminTable.objects.get(email=email)
            if password == user.password:
                request.session.clear()
                request.session['admin_id'] = user.admin_id
                return redirect('admindashboard')
            else:
                return render(request, 'adminlogin.html', {"error": "wrong password"})
        except AdminTable.DoesNotExist:
            return render(request, 'adminlogin.html', {"error": "you dont have an account"})
    try:
        admin_id = request.session['admin_id']
        try:
            AdminTable.objects.get(admin_id=admin_id)
            return redirect('admindashboard')
        except AdminTable.DoesNotExist:
            return render(request, 'adminlogin.html')
    except KeyError:
            return render(request, 'adminlogin.html')

# for user validation
def checkuser(email):
    users = UserTable.objects.all()
    for x in users:
        if x.email == email:
            return False
    return True

# return homepage for user that is not logged in
def home(request):
    try:
        id = request.session['id']
        try:
            UserTable.objects.get(id=id)
            return redirect('userdashboard')
        except UserTable.DoesNotExist:
            return render(request, 'home.html')
    except KeyError:
            return render(request, 'home.html')

# login user if details are correct redirect to user dashboard and if user is already login, redirect to userdashboard
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserTable.objects.get(email=email)
            if password == user.password:
                request.session.clear()
                request.session['id'] = user.id
                return redirect('userdashboard')
            else:
                return render(request, 'login.html', {"error": "wrong password"})
        except UserTable.DoesNotExist:
            return render(request, 'login.html', {"error": "you dont have an account"})
    try:
        id = request.session['id']
        try:
            UserTable.objects.get(id=id)
            return redirect('userdashboard')
        except UserTable.DoesNotExist:
            return render(request, 'login.html')
    except KeyError:
            return render(request, 'login.html')

# register new users only, but only if no one is logged in
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        image = request.FILES.get('image', '')
        password = request.POST['password']
        passwordone = request.POST['passwordone']
        role = request.POST['role']
        phone = request.POST['phone']

        if passwordone == password:
            if checkuser(email):
                new_user = UserTable(
                name=name,
                email=email,
                image=image,
                password=password,  
                role=role,
                phone=phone
                )
                new_user.save()
                return render(request, 'login.html', {"message": "Account created successfully!"})
            else:
                return render(request, 'signup.html', {"error": "Email already exists"})
        else:
            return render(request, 'signup.html', {"error": "Passwords do not match"})
    try:
        id = request.session['id']
        try:
            UserTable.objects.get(id=id)
            return redirect('userdashboard')
        except UserTable.DoesNotExist:
            return render(request, 'signup.html')
    except KeyError:
            return render(request, 'signup.html')

def logout(request):
    request.session.clear()
    return redirect('home')

# help user to regenerate new password via email
def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if not checkuser(email):
            user = UserTable.objects.get(email=email)
            user.password = random.randint(100000, 999999)
            user.save()
            send_email(f'{user.email}', f'there {user.name} your new password is {user.password}, use it to unlock your account you are advice to change it after that','Reset Password')
            return render(request, 'forgetpassword.html', {'success':True})
    try:
        id = request.session['id']
        return redirect('userdashboard')
    except KeyError:
        return render(request, 'forgetpassword.html')