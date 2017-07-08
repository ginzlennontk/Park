from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Animal
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext


def page_not_found(request):
    response = render_to_response('park/no_page.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def index(request):
    return render(request, 'park/home.html',
           {'all_animal':Animal.objects.filter(status="Published").count(),
            'mammal_num':Animal.objects.filter(status="Published",class_name="Mammal").count(),
            'reptile_num':Animal.objects.filter(status="Published",class_name="Reptile").count(),
            'bird_num':Animal.objects.filter(status="Published",class_name="Bird").count(),
            'fish_num':Animal.objects.filter(status="Published",class_name="Fish").count(),
            'amphibian_num':Animal.objects.filter(status="Published",class_name="Amphibian").count()})

def animal_list(request, class_name):
    all_class = ["All","Mammal","Reptile","Bird","Fish","Amphibian"]
    if(class_name == 'All'):
        list = Animal.objects.filter(status="Published").order_by('thai_name')
    elif(class_name in ('Mammal','Reptile','Bird','Fish','Amphibian')):
        list = Animal.objects.filter(status="Published",class_name=class_name).order_by('thai_name')
    else:
        return render(request, 'park/no_page.html')
    return render(request, 'park/animal_list.html',{'lists':list,'all_class':all_class,'class_now':class_name})
 
def animal_data(request, animal_name):
    try:
        animal = Animal.objects.get(name=animal_name.replace('_', ' '))
        image_list = animal.image.filter(status="Published").order_by('image')
        if(animal.status == "Published"):
            return render(request, 'park/animal_data.html',{'animal':animal,'image_list':image_list})
        else:
            raise
    except:
        return render(request, 'park/no_page.html')

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
            animal_list = Animal.objects.filter(Q(status="Published",) &
                (
                Q(thai_name__icontains=word) |
                Q(name__icontains=word,) |
                Q(class_name__icontains=word,) |
                Q(order__icontains=word) |
                Q(family__icontains=word) |
                Q(info__icontains=word) |
                Q(habitat__icontains=word)
                )
            )
        else:
            search_by = request.GET.get('search')
            animal_list = Animal.objects.filter(Q(status="Published") & filter_list[search_by])

    return render(request, 'park/search.html',{'word':word, 'lists':animal_list})

def add_pending(request):
    error_message = ""
    complete_message = ""
    if(request.POST.get('submit')):
        if("" in (request.POST.get('name'),request.POST.get('thai_name'))):
            error_message = "กรุณากรอกชื่อของสัตว์ด้วยจ้า"
        else:
            animal = Animal(thai_name = request.POST.get('thai_name'),
                            name = request.POST.get('name'),
                            class_name = request.POST.get('class_name'),
                            order = request.POST.get('order'),
                            family = request.POST.get('family'),
                            info = request.POST.get('info'),
                            habitat = request.POST.get('habitat'),
                            status= "Pending")
            animal.save()

            for pic in request.FILES.getlist('pic_file'):
                animal.image.create(image=pic)
            
            complete_message = "ขอบคุณที่ช่วยเพิ่มข้อมูลให้กับเรา :)"
    return render(request, 'park/add_data.html',{'error_message':error_message,'complete_message':complete_message})

def add_picture(request,animal_name):
    animal = Animal.objects.get(name=animal_name.replace('_', ' '))
    for pic in request.FILES.getlist('pic_file'):
            animal.image.create(image=pic,status="Pending")
    image_list = animal.image.filter(status="Published").order_by('image')
    
    return HttpResponseRedirect(reverse('park:animal_data', args=(animal_name,)))

def about(request):
    return render(request, 'park/about.html')
