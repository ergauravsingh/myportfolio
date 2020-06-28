from django.shortcuts import render, get_object_or_404
from .models import Project, Blog
from .forms import ContactForm


def index(request):
    projects = Project.objects.all()
    blogs = Blog.objects.order_by('-date')
    
    context = {
        'projects':projects,
        'blogs':blogs,
    }
    return render(request, 'project/index.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog':blog
    }
    return render(request, 'project/blog_details.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project':project
    }
    return render(request, 'project/project_details.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            return render(request, 'project/contactform.html', {'form': form})
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'project/contactform.html', context)


