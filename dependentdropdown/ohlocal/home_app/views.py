from django.http import JsonResponse
from django.shortcuts import render
from .forms import PersonCreationForm
from .models import Person, City


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            alert = 1
            form = PersonCreationForm()
            return render(request, 'home.html', {'form': form, 'alert':alert})
    return render(request, 'home.html', {'form': form})


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'list.html', {'persons':persons})

def delete(request, pk):
    del_person = Person.objects.get(pk=pk)
    del_person.delete()
    persons = Person.objects.all()
    return render(request, 'list.html', {'persons':persons})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

