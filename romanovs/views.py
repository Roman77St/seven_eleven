from django.shortcuts import render
from .models import Tsar

def romanovs(request):
    tsars = Tsar.objects.all()
    context = {
        'tsars': tsars
        }
    
    return render(request, template_name='romanovs/romanov.html', context=context)
