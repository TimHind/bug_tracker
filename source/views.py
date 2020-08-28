from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from source.models import MyUser, Ticket
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from source.forms import LoginForm, AddTicketForm
# Create your views here.
@login_required
def index(request):
    my_tickets = Ticket.objects.all()
    return render(request, "index.html", {"tickets": my_tickets})

def ticket_detail(request, post_id):
    my_ticket = Ticket.objects.filter(id=post_id).first()
    return render(request, "ticket_detail.html", {"post": my_ticket})

def author_detail(request, user_name):
    current_auth = Ticket.objects.filter(filedby__username=user_name).first()
    my_tickets = Ticket.objects.filter(filedby__username=user_name)
    return render(request, "author_detail.html", {"auth": current_auth, "tickets": my_tickets})

def ticket_edit_view(request, post_id):
    ticket = Ticket.objects.get(id=post_id)
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            ticket.description = data['description']
            ticket.title = data['title']
            ticket.save()
        return HttpResponseRedirect(reverse("ticket_detail", args=[ticket.id]))
    
    data = {
        "title": ticket.title,
       "description": ticket.description
    }

    form = AddTicketForm(initial=data)
    return render(request, "add_ticket.html", {"form": form})

def invalid_ticket(request, post_id):
    ticket = Ticket.objects.get(id=post_id)
    ticket.status = "Invalid"
    ticket.assignedto = None
    ticket.completedby = None
    ticket.save()
    return redirect('ticket_detail', post_id)

def complete_ticket(request, post_id):
    ticket = Ticket.objects.get(id=post_id)
    ticket.completedby = request.user
    ticket.status = "Done"
    ticket.assignedto = None
    ticket.save()
    return redirect('ticket_detail', post_id)

def assign_ticket(request, post_id):
    ticket = Ticket.objects.get(id=post_id)
    ticket.status = "In-progress"
    ticket.assignedto = request.user
    ticket.completedby = None
    ticket.save()
    return redirect('ticket_detail', post_id)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("home")))

    form = LoginForm()
    return render (request,  "login_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def add_ticket(request):
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title = data.get("title"),
                description = data.get("description"),
                filedby = request.user,
                assignedto = None,
                completedby = None,
            )
            if add_ticket:
                return redirect('/')
    form = AddTicketForm()
    return render(request, "add_ticket.html", {"form": form})