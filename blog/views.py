from django.shortcuts import render_to_response
from blog.models import Articulo, Comentario
from forms import ArticuloForm, ComentarioForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone



def home(request):
   entradas = Articulo.objects.all()[:10]
   return render_to_response('index.html', {'articulos' : entradas})

def crear(request):
    if request.POST:
    	form = ArticuloForm(request.POST)
       	if form.is_valid():
       		form.save()

          	return HttpResponseRedirect('/')
    else:
       	form = ArticuloForm()
     
    args = {}
    args.update(csrf(request))
    
    args['form'] = form

    return render_to_response('crear_articulo.html', args)

def articulos(request):
  return render_to_response('index.html', {'articulos' : Articulo.objects.all() })

def articulo(request, articulo_id=1):
  return render_to_response('articulo.html', {'articulo' : Articulo.objects.get(id=articulo_id) })

def agregar_comentario(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)

    if request.POST:
      form = ComentarioForm(request.POST)
      if form.is_valid():
        comentario = form.save(commit=False)

        comentario.fecha_pub = timezone.now()
        comentario.articulo = articulo

        comentario.save()

        return HttpResponseRedirect('/articulos/obtener/%s' % articulo_id)
    else:
        form = ComentarioForm()
     
    args = {}
    args.update(csrf(request))
    
    args['articulo'] = articulo
    args['form'] = form

    return render_to_response('agregar_comentario.html', args)

