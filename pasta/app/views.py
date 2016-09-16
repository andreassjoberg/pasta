"""
Definition of views.
"""

from .models import ProgramStat
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Pasta',
            'subtitle':'PAyroll STAtistics',
            'year':datetime.now().year,
            'stats':','.join(ProgramStat.objects.values_list('program_name', flat=True)),
            #'data':','.join(ProgramStat.objects.values_list('program_started_datetime', flat=True)),
        }
    )
