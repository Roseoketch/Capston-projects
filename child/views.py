from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import categories, organization
from .forms import CreateProfileForm
# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    if 'organization' in request.GET and request.GET["organization"]:
        search_term = request.GET.get("organization")
        searched_name = Organization.search_organization(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"organization":searched_organization})

    else:
        message = 'You havent searched for any term'
    return render(request,'search.html',{"message",message})


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = current_user
            new.save()
            return redirect(organization)
    else:
        form = CreateProfileForm()
    return render(request, 'profile/create_new.html', {"upload_form":form})



# def organization_by_categories(request):
