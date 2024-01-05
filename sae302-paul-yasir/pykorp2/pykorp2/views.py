from django.shortcuts import render

def pykorp_render(request):
    #affichage de la page initiale
    if request.method=="GET":
        page=render(request, "login.html")

    #traitement du remplissage d'un formulaire
    if request.method=="POST":
        #quel formulaire a été remplit ?
        type=request.POST["colis_ou_login_input"]
        
        if type=="colis":
            #récupération de l'id du colis tapé
            ID_colis=request.POST["ID_colis_input"]

        else:
            #récupération de l'id et du mot de passe tapé
            uid=request.POST["UID_input"]
            pwd=request.POST["PWD_input"]
            if #dans la base de donnée: id => mdp hashé = correct :
                #renvoie vers page associée, localhost:8000/pykorp/ID/main

            else:
                page=render(request, "login.html")


def suivi_render(request):
    page=render(request, "suivi_colis.html")
    return page


def pykorp_render(request):
    page=render(request, "pykorp.html")
    return page







def login_render(request):
    if request.method=="GET":
        page=render(request, "login.html")
    if request.method=="POST":
        #récupération de l'id et du mot de passe tapé
        id=request.POST["ID_input"]
        pwd=request.POST["PWD_input"]
        if #dans la base de donnée: id => mdp hashé = correct :
            #renvoie vers page associée, localhost:8000/pykorp/ID/main

        else:
            page=render(request, "login.html")