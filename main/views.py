from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Job, Blog, ContactMessage, TeamMember
from .forms import ContactForm, DriverForm

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'main/index.html', {'blogs': blogs})

def about(request):
    return render(request, 'main/about.html')

def faq(request):
    return render(request, 'main/faq.html')

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'main/team.html', {'team_members': team_members})

def career(request):
    jobs = Job.objects.all()
    return render(request, 'main/career.html', {'jobs': jobs})

def blog(request):
     blogs = Blog.objects.all().order_by('-created_at')
     return render(request, 'main/blog.html', {'blogs': blogs})

def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    latest_blogs = Blog.objects.exclude(id=id).order_by('-created_at')[:4]
    return render(request, 'main/blog_details.html', {'blog': blog, 'latest_blogs': latest_blogs})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return render(request, 'main/contact.html', {'form': form, 'success': True})
        else:
            return render(request, 'main/contact.html', {'form': form, 'error': True})
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def signup_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')
    else:
        form = DriverForm()

    return render(request, 'main/signup.html', {'form': form})

def signup_success(request):
    return render(request, 'main/signup_success.html')