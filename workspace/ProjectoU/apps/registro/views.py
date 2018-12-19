from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.core.mail import EmailMessage
# Create your views here.

def index(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            
            rut = "Rut : " + post.rut
            correo = "Correo : " + post.correo
            fecha  = "Fecha Registro : " + str(post.fecha_registro)
            razon = "Correo : " + post.razon_social
            listado = "Listado Documento :" + str(post.listado_docuemento)
            mensaje = "Solicitud de registro los datos son los siguentes : \n " + rut +"\n "+ correo +"\n "+ fecha +"\n "+ razon + "\n " + listado

            email = EmailMessage('Registro Comercio Multicaja', mensaje, to=['ignaciojaviermunozv@gmail.com'])
            email.send()

            return render(request,'registro/success.html')
    else:
        form = PostForm()
    
    return render(request, 'registro/index.html', {'form': form})