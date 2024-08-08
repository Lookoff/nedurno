from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
    
    # return HttpResponse(''.join([str(course) + '<br>' for course in courses]))
    # cards = Card.objects.all()
    # return HttpResponse(''.join([str(card) + '<br>' for card in cards]))

def single_course(request, course_id):
    #OPTION 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()
    
    #OPTION 2
        course = get_object_or_404(Course, pk=course_id)
        return render(request, 'single_course.html', {'course': course})