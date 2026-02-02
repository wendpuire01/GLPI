from django.shortcuts import render,redirect, get_object_or_404
from .forms import ComputerForm,AttributionForm,LicenceForm
from .models import Ordinateur,Personne,Mouvement,Licences,Panne,Histo
from django.db import connection
from django.contrib.auth import login as auth_login ,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit

import os
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.db.models import Count






# Create your views here.
@login_required
def index(request):
    Ordinateurs=len(Ordinateur.objects.all())
    licences=len(Licences.objects.all())
    personne=len(Personne.objects.all())
    pannes=len(Panne.objects.all())
    return render(request,'index.html')

@login_required
def print_inventaire(request):
    # Récupérer tous les objets Ordinateur
    ordinateurs = Ordinateur.objects.all()
    
    # Charger le template
    template = get_template('inventaire_print.html')
    
    # Rendre le HTML avec les variables de contexte
    context = {'ordinateurs': ordinateurs}
    html = template.render(context)
    
    # Options de format du PDF
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        "enable-local-file-access": ""
    }
    
    # Générer le PDF
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, options,configuration=pdfkit_config)
    
    # Créer la réponse HTTP avec le PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="inventaire.pdf"'
    
    return response


def login(request):
    logout(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

class CustomLoginView(login):
    def form_invalid(self, form):
        messages.error(self.request, 'Nom d’utilisateur ou mot de passe incorrect.')
        return super().form_invalid(form)

@login_required    
def home(request):
    return render(request, 'index.html')

@login_required
def inventaire(request):
    return render(request, 'inventaire.html')

@login_required
def acquisition(request):
    ordinateur=Ordinateur.objects.all()
    if request.method == 'POST':
        marque=request.POST['marque']
        date=request.POST['date']
        ram=request.POST['ram']
        ecran=request.POST['ecran']
        disque=request.POST['disque']
        processeur=request.POST['Processeur']
        numero_serie= request.POST['seri']
        ord= Ordinateur(marque=marque,dte_acquisition=date,ecran=ecran,ram=ram,disque_dur=disque,processeur=processeur,numero_serie=numero_serie)
        ord.save()
   

    return render(request, 'acquisition.html', {'ordinateur':ordinateur})
    

@login_required
def attribution(request):
    ordinateurs=Ordinateur.objects.all()
    personnes= Personne.objects.all()
    attribution=Mouvement.objects.all()
    """
    if request.method=="POST":
        ordinateur=request.POST['ordinateur']
        utilisateur=request.POST['utilisateur']
        motifs=request.POST['motif']
        date=request.POST['date']  
        mouv= Mouvement(ordinateur=ordinateur,utilisateur=utilisateur,motifs=motifs,date=date)
        mouv.save()  
    """
    form=AttributionForm()
    if request.method=="POST":
        form=AttributionForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()

    return render(request, 'attribution.html',{'form':form,'attributions':attribution})

@login_required(login_url='/login/')
def dashboard(request):
    licences = Licences.objects.all()
    return render(request, 'index.html')

@login_required(login_url='/login/')
def panne(request):
    
    Pannes = Panne.objects.all()
   
    return render(request,'list_panne.html',{'Pannes':Pannes})

@login_required(login_url='/login/')
def licence(request):
    return render(request, 'Licence.html')

@login_required(login_url='/login/')
def personne(request):
    personnes=Personne.objects.all()
    
    if request.method=="POST":
        nom=request.POST['name']
        prenom=request.POST['prenom']
        telephone=request.POST['telephone']
        departement=request.POST['departement']
        poste=request.POST['poste']
        pers=Personne(nom=nom,prenom=prenom,telephone=telephone,departement=departement,poste=poste)
        pers.save()
    return render(request,'personne.html',{'personnes':personnes})

@login_required(login_url='/login/')
def licence_list(request):
    licences = Licences.objects.all()
    if request.method == 'POST':
        form = LicenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('licence_list')
    else:
        form = LicenceForm()
    
    return render(request, 'licence_list.html', {'licences': licences,'form': form})

@login_required(login_url='/login/')
def toggle_visibility(request, pk):
   licence = get_object_or_404(Licences, pk=pk)
   if request.method == 'POST':
        licence.delete()
        return redirect('licence_list')
    
   return redirect('licence_list')


    
def de_maintenance(request):
    #Pannes=Panne.objects.all()
    Pannes = Panne.objects.all()
    if request.method=="POST":
        utilisateur= request.POST['utilisateur']
        marque=request.POST['marque']
        date=request.POST['date']
        telephone=request.POST['telephone']
        departement=request.POST['departement']
        intitule=request.POST['prbl']
        nombre=request.POST['nbr']
        statut=request.POST['statut']
        numero_seri=request.POST['seri']
        pan=Panne(date=date,intitule=intitule,telephone=telephone,departement=departement,marque=marque,nombre=nombre,utilisateur=utilisateur,statut=statut,numero_seri=numero_seri)
        pan.save()
        
    return render (request,'maintenance.html',{'Pannes':Pannes})

@login_required(login_url='/login/')
def modifier_personne(request, id):
    personne = get_object_or_404(Personne, id=id)
    if request.method == 'POST':
        personne.nom = request.POST['nom']
        personne.nom = request.POST['prenom']
        personne.nom = request.POST['departement']
        personne.nom = request.POST['poste']
        personne.nom = request.POST['telephone']
        personne.save()
        return redirect('personne')  # Redirect to the class management page
    #return render(request, 'modifier_classe.html', {'classe': classe})



@login_required(login_url='/login/')
def supprimer_personne(request, pk):
    personne = get_object_or_404(Personne, pk=pk)
    #if request.method == 'POST':
    personne.delete()
    return redirect('personne')

def machines_par_mois(request):
    machines = (
        Ordinateur.objects.annotate(mois=TruncMonth('date_acquisition'))
        .values('mois')
        .annotate(total=Count('id'))
        .order_by('mois')
    )

    # Extraire les mois et les totaux pour envoyer au graphique
    labels = [machine['mois'].strftime('%B %Y') for machine in machines]
    data = [machine['total'] for machine in machines]

    return JsonResponse({
        'labels': labels,
        'data': data,
    })