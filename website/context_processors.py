from .models import Department

def active_departments(request):
    return {
        'header_departments': Department.objects.filter(status='published')
    }
