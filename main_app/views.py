from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Bird, NestingMaterial
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return(render(request, 'about.html'))

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    id_list= bird.nestingmaterials.all().values_list('id')
    nestingmaterials_bird_doesnt_have = NestingMaterial.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'birds/detail.html', {
        'bird': bird,
        'feeding_form': feeding_form,
        'nestingmaterials': nestingmaterials_bird_doesnt_have
        })

def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    return redirect('detail', bird_id=bird_id)

class NestingMaterialList(ListView):
    model = NestingMaterial

class NestingMaterialDetail(DetailView):
    model = NestingMaterial

class NestingMaterialCreate(CreateView):
    model = NestingMaterial
    fields = '__all__'
    
class NestingMaterialUpdate(UpdateView):
    model = NestingMaterial
    fields = ['name', 'color']
    
class NestingMaterialDelete(DeleteView):
    model = NestingMaterial
    success_url = "/nesting-materials"
    
def assoc_nestingmaterial(request, bird_id, nestingmaterial_id):
    Bird.objects.get(id=bird_id).nestingmaterials.add(nestingmaterial_id)
    return redirect('detail', bird_id=bird_id)

def unassoc_nestingmaterial(request, bird_id, nestingmaterial_id):
    Bird.objects.get(id=bird_id).nestingmaterials.remove(nestingmaterial_id)
    return redirect('detail', bird_id=bird_id)

class BirdCreate(CreateView):
    model = Bird
    fields = "__all__"
    
class BirdUpdate(UpdateView):
    model = Bird
    fields = "__all__"

class BirdDelete(DeleteView):
    model = Bird
    success_url = "/birds"