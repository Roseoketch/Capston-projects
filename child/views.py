from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Contact, Organization,Program
from .forms import CreateProfileForm
from django.shortcuts import render_to_response
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
    return render(request, 'profile/create_new.html', {"upload_form":form, "current_user":current_user})

#
# Volunteer views

def volunteersIndex(request):
	volunteer_list = Volunteer.objects.all()
	return render_to_response('templates/users/volunteer/index.html', {'volunteer_list': volunteer_list})

def volunteerDetails(request, volunteer_id):
	v = Volunteer.objects.get(id=volunteer_id)
	return render_to_response('templates/users/volunteer/details.html', {'volunteer':v})

# Organizer views
@login_required(login_url='/accounts/login/')
def organizationIndex(request):
        contact = Contact.objects.all()
        program = Program.objects.all()
        organization_list = Organization.objects.all()
        print(organization_list)
        return render_to_response('organizer/index.html', {'organization_list': organization_list, "contact":contact, "program":program})

@login_required(login_url='/accounts/login/')
def organizationDetails(request, organization_id):
        o = get_object_or_404(Organization, ok = organization_id)
        return render_to_response('organizer/details.html', {'organization': o})

# Event views

def eventsIndex(request):
        event_list = Event.objects.all()
        return render_to_response('users/event/index.html', {'event_list': event_list})

def eventDetails(request, event_id):
        e = get_object_or_404(Event, ek = event_id)
        return render_to_response('users/event/details.html', {'event': e})
