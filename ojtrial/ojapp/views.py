from django.shortcuts import render
from django.http import Http404,HttpResponse
from .models import Problem
# Create your views here.
def index(request):
    all_problems = Problem.objects.all()
    context = {
        'all_problems': all_problems,
    }
    return render(request, 'ojapp/index.html', context)

def detail(request, problem_id):
    try:
        problem = Problem.objects.get(pk=problem_id)
    except Problem.DoesNotExist:
        raise Http404("Problem does not exist")
    return render(request, 'ojapp/details.html', {'problem': problem})

def verdict(request, problem_id):
    response = "You're looking at the verdict of question %s."
    return HttpResponse(response % problem_id)

def submit(request, problem_id):
    return HttpResponse("You're submitting solution for question %s." % problem_id)