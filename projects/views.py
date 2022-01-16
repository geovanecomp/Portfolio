from django.views import generic

from .models import Project


class IndexView(generic.ListView):
    template_name = 'projects/index.html'

    def get_queryset(self):
        """Returns all projects ordered by priority"""
        return Project.objects.order_by('-priority_order')

class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

# def index(request):
#     projects = Project.objects.order_by('priority_order')
#     return render(request, 'projects/index.html', {'projects': projects})


# def detail(request, project_id):
#     project = get_object_or_404(Project, pk=project_id)
#     return render(request, 'projects/detail.html',{'project': project})
