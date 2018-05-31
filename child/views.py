from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import categories, organization

# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    profile = MyUser.get_user()

    if 'organization' in request.GET and request.GET["organization"]:
        search_term = request.GET.get("organization")
        searched_name = Organization.search_organization(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"organization":searched_organization})

    else:
        message = 'You havent searched for any term'
    return render(request,'search.html',{"message",message})
