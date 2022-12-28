from django.shortcuts import render
from .models import Shop, Rubrics
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    rubrics = Rubrics.objects.all()
    posts = Shop.objects.all()
    
    return HttpResponse(template.render({'posts' : posts, 'rubrics': rubrics,}, request))


def by_rubric(request, rubric_id):
    laptops = Shop.objects.filter(rubric=rubric_id)
    rubrics = Rubrics.objects.all()
    current_rubric = Rubrics.objects.get(id=rubric_id)

    return render(request, '.html', {'laptops': laptops, 'rubrics': rubrics, 'current_rubric': current_rubric})
