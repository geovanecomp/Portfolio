from django.http import HttpResponse
from .models import Project


def index(request):
    projects = Project.objects.order_by('-pub_date')
    return HttpResponse(projects)


def detail(request, project_id):
    return HttpResponse("Welcome to project with id: %s" % project_id)
