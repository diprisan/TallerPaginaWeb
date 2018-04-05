from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.template import Template , Context
from django.shortcuts import render_to_response
from django.template                import RequestContext
from json import dumps
from .models import Usuarios
from .models import Question
from .models import galeria
from .models import nacionalesextranjeros
from .models import ventas_totales
from django.http import JsonResponse
#from django.core import serializers
import sys
import json
from rest_framework import serializers
def index(request):
    return HttpResponse("Hello, world. You're at twhe polls index.")
	
def results(request, question_id):
    response = "Tu pregunta es %s."
    return HttpResponse(response % question_id)

def indice(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse(" Tu ves la pregunta %s." % question_id)

def detailsExcep(request, question_id):
        queryId = Question.objects.get(id=question_id)
        return HttpResponse(queryId.question_text)
	
def indexRender(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def home(request):
    template = loader.get_template('polls/home.html')
    context = {
           }
    return HttpResponse(template.render(context, request))

def Rootindex(request):
    template = loader.get_template('polls/Rootindex.html')
    context = {
           }
    return HttpResponse(template.render(context, request))

def reporte(request, user_id):
    if "usuario" in request.session:
        #template = loader.get_template('polls/Reporte.html')
        context = {
            'user_id': user_id
           }
        return render(request, 'polls/Reporte.html', context)
        #return HttpResponse(template.render(context, request))
    else:
        context = {}
        return render(request, 'polls/no_sesion.html', context)

def no_sesion(request):
    template = loader.get_template('polls/no_sesion.html')
    context = {
           }
    return HttpResponse(template.render(context, request))

def no_login(request):
    template = loader.get_template('polls/no_login.html')
    context = {
           }
    return HttpResponse(template.render(context, request))
def login2(request):
    template = loader.get_template('polls/login2.html')
    context = {
           }
    return HttpResponse(template.render(context, request))


def login(request):
    message = None
    if request.method == 'POST':
      username_post = request.POST['username']
      password_post = request.POST['password']
      user = authenticate ( username = username_post, password = password_post)
      if user is not None:
        login_django( request, user)
        #return redirect('polls:dashboard')
        return HttpResponseRedirect(reverse('polls:dashboard'))
      else:
        menssage = "incorrecto"
        #return redirect('polls:login')
        return HttpResponseRedirect(reverse('polls:login'))

      form = LoginForm()
      context = {
        'form' : form,
        'message' : message
      }
      return  render_to_response (request, 'polls/login.html',   {'form': form})
 


def dashboard(request):
   return render (request, 'polls/dashboard.html', {})
#, usuario, contra):

def loginGar(request, username=None):
    contra=""
    valor="";
    #queryId = Usuarios.objects.get(user=username, passw=contra)
    try:   queryId = Usuarios.objects.get(id=1)
    #template = loader.get_template('polls/home.html')
    #context = {   }
    #return HttpResponse(template.render(context, request))
    except DoesNotExist:
                valor="Hello, world. You're at twhe polls index."

def detailsLogin(request, user_id ,pass_id):
    valor="trae datos"
    try:     
        userId = Usuarios.objects.filter(user=user_id)
        userId = userId.filter(passw=pass_id)
        #return HttpResponseRedirect(reverse('polls:home'))
        #context = {'latest_question_list': userId}
        #return render(request, 'polls/index.html', context)
        if userId:
            context = {'latest_question_list': userId}
            request.session["usuario"] = user_id
            return redirect('http://127.0.0.1:8000/polls/reporte/'+user_id+'/')

        else:
            return redirect('http://127.0.0.1:8000/polls/no_login/')

    #print ("The answer is", 2*2) id=question_id,
    except Exception as e:
                valor="failed to: %s" % (str(e))
    return HttpResponse(valor)

def verGaleria(request, idGaleria):
    if request.method == 'GET':
        try:
            galerJson = galeria.objects.filter(id_hotel=idGaleria)
            if galerJson:
                serializer = GaleriaSerializer(galerJson, many=True)
                return JsonResponse(serializer.data, safe=False)
                #return HttpResponse("hola")
            else:
                return HttpResponse("No hay datos")
        except Exception as e:
                valor="falla en galeria to: %s" % (str(e))
                return HttpResponse(valor)
    else:
        return HttpResponse("Peticion no valida")

class GaleriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = galeria
		fields = '__all__'

class ventaSerializer(serializers.ModelSerializer):
	class Meta:
		model = ventas_totales
		fields = '__all__'

def verVenta (request, idHotel, idanio):
    if request.method == 'GET':
        try:
            ventasJson = ventas_totales.objects.filter(id_hotel=idHotel).filter(anio=idanio)

            if ventasJson:
                serializer = ventaSerializer(ventasJson, many=True)
                #print ("hola2")
                return JsonResponse(serializer.data, safe=False)
                #return HttpResponse(ventasJson.normal)
            else:
                return HttpResponse("No hay datos")
        except Exception as e:
            valor = "falla en ventas to: %s" % (str(e))
            return HttpResponse(valor)
    else:
        return HttpResponse("Peticion no valida")

class nacSerializer(serializers.ModelSerializer):
	class Meta:
		model = nacionalesextranjeros
		fields = '__all__'

def vernac (request, idHotel, idanio):
    if request.method == 'GET':
        try:
            nacJson = nacionalesextranjeros.objects.filter(id_hotel=idHotel).filter(anio=idanio)

            if nacJson:
                serializer = nacSerializer(nacJson, many=True)
                print ("hola2")
                return JsonResponse(serializer.data, safe=False)
                #return HttpResponse(ventasJson.normal)
            else:
                return HttpResponse("No hay datos")
        except Exception as e:
            valor = "falla en ventas to: %s" % (str(e))
            return HttpResponse(valor)
    else:
        return HttpResponse("Peticion no valida")

                  
