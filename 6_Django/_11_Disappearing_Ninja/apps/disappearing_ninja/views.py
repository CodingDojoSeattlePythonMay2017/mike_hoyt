from django.shortcuts import render

def index(request):
    return render( request, "disappearing_ninja/index.html" )

def ninjas(request):
    return render( request, "disappearing_ninja/ninjas.html" )

def ninja_select(request, ninja_color):
    context = { 'img_src': "disappearing_ninja/img/notapril.jpg" }
    if ninja_color.lower() == "purple":
        context['img_src'] = "disappearing_ninja/img/donatello.jpg"
    elif ninja_color.lower() == "blue":
        context['img_src'] = "disappearing_ninja/img/leonardo.jpg"
    elif ninja_color.lower() == "orange":
        context['img_src'] = "disappearing_ninja/img/michelangelo.jpg"
    elif ninja_color.lower() == "red":
        context['img_src'] = "disappearing_ninja/img/raphael.jpg"
    return render( request, "disappearing_ninja/ninja_select.html", context )
