from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

# def user_login(request):
#     if request.method == 'POST':
#         # Retrieve the username and password from the request
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Authenticate the user
#         user = authenticate(request, Username=username, Password=password)

#         # Check if authentication was successful
#         if user is not None:
#             # Log the user in
#             login(request, user)
#             return redirect('/')
#         else:
#             messages.error(request, 'Invalid username or password.')
#             return render(request, 'user/login.html')

#     else:
#         return render(request, 'user/login.html')


# def user_signup(request, id=0):
#     if request.method == "GET":
#         if id==0:
#             form = UserForm()
#         else:
#             user = User.objects.get(pk=id)
#             form = UserForm(instance=user)
#         return render(request, 'user/signup.html', {'form':form})
#     else:
#         if id==0:
#             form = UserForm(request.POST)
#         else:
#             user = User.objects.get(pk=id)
#             form = UserForm(request.POST,instance=user)
#         if form.is_valid():
#             form.save()
#         return redirect('/')

# def user_signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         gender = request.POST['gender']
#         email = request.POST['email']
#         mobile_no = request.POST['mobile_no']
#         nic = request.POST['nic']
#         nationality = request.POST['nationality']
#         address = request.POST['address']
#         if password ==confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'username exist')
#                 return redirect(user_signup)
#             else:
#                 user = User.objects.create_user(username=username, password=password, email=email,firstname=firstname,lastname=lastname,gender=gender,mobile_no=mobile_no,nic=nic,nationality=nationality,address=address)
#                 user.set_password(password)
#                 user.save()
                
#                 return redirect('user_login')
#     else:
#         print("this is no post")
#     return render(request,"user/signup.html")

# def user_login(request):
#     if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']

#        user = auth.authenticate(username=username, password=password)

#        if user is not None:
#            auth.login(request, user)
#            return redirect('/')
#        else:
#            messages.info(request, 'Invalid')
#            return redirect('user_login')

#     else: 
#         return render(request,'user/login.html')


# CRUD
def user_list(request):
    users = User.objects.all()
    # users_count = users.count()
    context = {
        'user_list':users,
    }
    return render(request,'user/user_list.html',context)

def user_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = UserForm()
        else:
            user = User.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(request, 'user/user_form.html', {'form':form})
    else:
        if id==0:
            form = UserForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('/user/list')

def user_delete(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('/user/list')