from courses.models import Course
from django.views.generic import ListView
from django.shortcuts import render

class HomePageView(ListView):
    template_name = "courses/home.html"
    queryset = Course.objects.filter(active=True)
    context_object_name = 'courses'

def contact(request):
    return render(request, 'contact.html')
