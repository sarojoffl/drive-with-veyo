from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Job, Blog, ContactMessage, TeamMember
from .forms import ContactForm, UserForm
from django.core.paginator import Paginator
from django.conf import settings

def index(request):
    blogs = Blog.objects.order_by('-created_at')[:3]
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

    # Set up pagination: 6 blogs per page
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/blog.html', {'page_obj': page_obj})

def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    latest_blogs = Blog.objects.exclude(id=id).order_by('-created_at')[:4]
    return render(request, 'main/blog_details.html', {'blog': blog, 'latest_blogs': latest_blogs})

def contact(request):
    context = {
        'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            context['success'] = True
        else:
            context['error'] = True
        return render(request, 'main/contact.html', context)
    else:
        context['form'] = ContactForm()
        return render(request, 'main/contact.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')
    else:
        form = UserForm()

    return render(request, 'main/signup.html', {'form': form})

def signup_success(request):
    return render(request, 'main/signup_success.html')