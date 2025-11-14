from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto

# Create your views here.(controladores-> logica)
def index_proyecto(request):
    #ORM
    proyectos = Proyecto.objects.all()# select * from productos;
    context = {
        'lista_proyectos': proyectos
    }
    return render(request,'index.html',context)

def crear_proyecto(request):
    
    if request.method=='GET':
        return render(request,'crear_proyecto.html')
    
    if request.method == 'POST':
        pass
    

def editar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, pk=id)
    return render(request,'editar_proyecto.html')

def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    proyecto.delete()
    
    return redirect('index_proyecto')