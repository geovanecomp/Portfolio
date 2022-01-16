""" 
Ideally I am used to create different test files (at least one for each model or view), but
as my intention here is to be practical and direct, I am doing just a few tests in the same file.
"""
import datetime
from django.test import TestCase, Client
from django.urls import reverse
from .models import Project
from .views import IndexView

client = Client()

def _get_valid_project():
    valid_project = {
        'title': 'Test 2',
        'summary': 'summary 2',
        'description': 'description 2',
        'image': 'images/cefet-rj.jpeg',
        'pub_date': datetime.datetime(2022, 1, 12, 0, 7, 42, tzinfo=datetime.timezone.utc),
        'repository_link': 'http://www.github.com/geovanecomp',
        'priority_order': 1
    }
    return valid_project


class ProjectIndextViewTests(TestCase):
    """
    The list of projects should be available properly
    """

    def test_empty_project_list(self):
        response = self.client.get(reverse('projects:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['project_list'], [])
        self.assertContains(response, "No projects available.")

    def test_project_list_after_project_insertion(self):
        project = Project.objects.create(**_get_valid_project())
        response = self.client.get(reverse('projects:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['project_list'], [project])
class ProjectIndexViewPriorityTests(TestCase):
    """
    The list of projects should be shown in the order defined
    by the priority field.
    """

    def setUp(self):
        # Defining a low priority project
        low_priority_project = _get_valid_project()
        low_priority_project['priority_order'] = 1
        Project.objects.create(**low_priority_project)

        # Defining a high priority project
        high_priority_project = _get_valid_project()
        high_priority_project['priority_order'] = 10
        Project.objects.create(**high_priority_project)

    def test_high_priority_projects_should_be_loaded_first(self): 
        response = self.client.get(reverse('projects:index'))
        projects = response.context['project_list']
        
        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(projects[1].priority_order, projects[0].priority_order)
        