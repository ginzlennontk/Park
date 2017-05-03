from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

from .models import Animal
from django.db.models import Q

def index(request):
    return render(request, 'park/home.html',
           {'all_animal':Animal.objects.all().count(),
            'mammal_num':Animal.objects.filter(class_name="Mammal").count(),
            'reptile_num':Animal.objects.filter(class_name="Reptile").count(),
            'bird_num':Animal.objects.filter(class_name="Bird").count(),
            'fish_num':Animal.objects.filter(class_name="Fish").count(),
            'amphibian_num':Animal.objects.filter(class_name="Amphibian").count()})

def animal_list(request, class_name):
    all_class = ["All","Mammal","Reptile","Bird","Fish","Amphibian"]
    if(class_name == 'All'):
        animal_list = Animal.objects.order_by('thai_name')
    elif(class_name in ('Mammal','Reptile','Bird','Fish','Amphibian')):
        animal_list = Animal.objects.filter(class_name=class_name).order_by('thai_name')
    else:
        raise Http404("Question does not exist")
    return render(request, 'park/animal_list.html',{'lists':animal_list,'all_class':all_class,'class_now':class_name})

def animal_data(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return render(request, 'park/animal_data.html',{'animal':animal})

def search(request):
    animal_list = []
    word = ""
    if(request.GET.get('word')):
        word = request.GET.get('word')
        filter_list = { 'name'  :   Q(name__icontains=word) | 
                                    Q(thai_name__icontains=word),
                        'order' :   Q(order__icontains=word),
                        'family':   Q(family__icontains=word),
                        'info'  :   Q(info__icontains=word),
                        'habitat':  Q(habitat__icontains=word)
                        }

        if(request.GET.get('search') == 'all'):
            animal_list = Animal.objects.filter(
                Q(thai_name__icontains=word) |
                Q(name__icontains=word,) |
                Q(class_name__icontains=word,) |
                Q(order__icontains=word) |
                Q(family__icontains=word) |
                Q(info__icontains=word) |
                Q(habitat__icontains=word)
            )
        else:
            search_by = request.GET.get('search')
            animal_list = Animal.objects.filter(filter_list[search_by])

    return render(request, 'park/search.html',{'word':word, 'lists':animal_list})

def add_pending(request):
    pass
    '''if(request.POST.get('submit')):
        animal = Pending(thai_name = request.POST.get('thai_name'),
                        name = request.POST.get('name'),
                        class_name = request.POST.get('class_name'),
                        order = request.POST.get('order'),
                        family = request.POST.get('family'),
                        info = request.POST.get('info'),
                        habitat = request.POST.get('habitat'),
                        picture = request.FILES.get('pic_file'))
        animal.save()'''
    return render(request, 'park/add_data.html')