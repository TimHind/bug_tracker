"""bugapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from source.views import login_view, index, logout_view, add_ticket, ticket_detail, author_detail, ticket_edit_view, complete_ticket, assign_ticket, invalid_ticket

urlpatterns = [
    path('', index, name="home"),
    path('addticket/', add_ticket),
    path('ticket/<int:post_id>/edit/', ticket_edit_view),
    path('ticket/<int:post_id>/', ticket_detail, name="ticket_detail"),
    path('auth/<str:user_name>/', author_detail),
    path('complete/<int:post_id>/', complete_ticket, name='completed'),
    path('assign/<int:post_id>/', assign_ticket, name='assign'),
    path('invalid/<int:post_id>/', invalid_ticket, name='invalid'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view),
    path('admin/', admin.site.urls),
]
