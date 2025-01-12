from django.shortcuts import render

# Exemple de données simulées
PROJECTS = [
    {'id': 1, 'title': 'Analyse des génomes', 'description': 'Étude approfondie des mutations humaines.'},
    {'id': 2, 'title': 'Modélisation des protéines', 'description': 'Création de modèles 3D de protéines.'},
]

def index(request):
    """Page d'accueil."""
    return render(request, 'index.html', {'projects': PROJECTS})

def about(request):
    """Page à propos."""
    return render(request, 'about.html')

def contact(request):
    """Page de contact."""
    return render(request, 'contact.html')

def project_detail(request, project_id):
    """Détails d'un projet spécifique."""
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    return render(request, 'project_detail.html', {'project': project})
