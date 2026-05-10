from .models import Department, DigitalLibrary, ProductionUnit, Tender, DeanMessage

def active_departments(request):
    return {
        'header_departments': Department.objects.filter(status='published')
    }
def published_digital_libraries(request):
    return {
        'digital_libraries': DigitalLibrary.objects.filter(status='published').order_by('-published_date')[:10]
    }
def published_production_units(request):
    return {
        'production_units': ProductionUnit.objects.filter(status='published').order_by('-published_date')[:10]
    }
def published_tenders(request):
    return {
        'tenders': Tender.objects.filter(status='published').order_by('-published_date')[:10]
    }
def dean_message(request):
    return {
        'dean_message': DeanMessage.objects.first()  # Assuming you want to display the first message
    }   