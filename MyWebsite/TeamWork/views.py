from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm, Todays_PlanForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile, Today_Todo
from django.contrib.auth.models import User


# Create your views here.


def Greetings(request):
    return render(request, "base.html")


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "TeamWork/Greetings.html")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "TeamWork/login.html", {"form": form})


def Welcome_Page(request):
    return render(request, "TeamWork/Greetings.html")


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data["password"])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(
                request, "TeamWork/register_done.html", {"new_user": new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(request, "TeamWork/register.html", {"user_form": user_form})


@login_required()
def Todays_Plan(request):
    Todays_plan_ = Today_Todo.objects.filter(Created_by=request.user)

    return render(request, "TeamWork/Today_Plan.html", {"Todo_list": Todays_plan_})


def Today_Plan_User_Input(request):
    if request.method == "POST":
        form = Todays_PlanForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            cd = form.cleaned_data
            new_todo = form
            # Set the chosen title and description
            new_todo.title = cd["title"]
            new_todo.description = cd["description"]
            # Save the User object
            # Create the user profile
            Today_Todo.objects.create(
                title=new_todo.title, description=new_todo.description
            )

            return render(
                request, "TeamWork/Updated_Todo.html", {"Todo_list": new_todo}
            )
    else:
        form = Todays_PlanForm()
    return render(request, "TeamWork/Add_Todays_Plan.html", {"form": form})
