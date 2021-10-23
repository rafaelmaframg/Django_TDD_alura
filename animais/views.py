
from django.shortcuts import render, redirect
from animais.models import Animal
# Create your views here.
def index(request):
    context = {'caracteristicas': None}
    if 'buscar' in request.GET:
        animais = Animal.objects.all()
        animal_pesquisado = request.GET['buscar']
        caracteristicas = animais.filter(nome_animal__icontains = animal_pesquisado )
        context = {'caracteristicas': caracteristicas}
    return render(request, 'index.html', context)

def cria_animal(request):
    if request.method == 'POST':
        nome_animal = request.POST['nome_animal']
        predador = request.POST['predador']
        venenoso = request.POST['venenoso']
        domestico = request.POST['domestico']
        animal = Animal.objects.create(nome_animal=nome_animal,
                                         predador=predador, venenoso=venenoso,
                                         domestico=domestico)
        animal.save()
        return redirect('index')
    else:
        return render(request, 'cria_animal.html')