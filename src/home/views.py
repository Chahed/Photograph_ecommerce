from django.shortcuts import render,get_object_or_404
from home.models import home_image, film, projet, realisation,cv , commissioned_work, shop
from home.forms import ClientForm


def index(request):
    im = home_image.objects.order_by()

    return render(request, 'index.html' , {'img':im})

def photographs(request):

    return render(request, 'photographs.html')


def films(request):

    list= film.objects.order_by()

    return render(request, 'films.html', {'films':list})

def contact(request):

    cv1 = cv.objects.order_by()

    return render(request, 'contact.html', {'cv':cv1})


def news(request):

    return render(request, 'news.html')

def projects(request):
    photos= projet.objects.order_by()

    list=[]

    for i in photos :
        list.append(i)

    return render(request, 'projects.html', {'photos':list})

def works(request):
    photos= commissioned_work.objects.order_by()
    list=[]
    for i in photos :
        list.append(i)



    return render(request, 'works.html', {'photos':list})

def consulter(request, id, id1):

    ph = get_object_or_404(projet,id=id)
    photoss= realisation.objects.order_by()
    list=[]

    for i in photoss :
        if i.projet == ph.titre :
            list.append(i)

    a = int(id1)
    photo=list[a]
    if a==0 :
        if len(list)==1 :
            nex=0
            pre=len(list)-1
        else:
            nex = a+1
            pre = len(list)-1
    else :
        if a== (len(list)-1):
            nex= 0
            pre= a-1
        else:
            nex=a+1
            pre=a-1

    next = str(nex)
    prev = str(pre)
    len1= len(list)
    return render(request, 'photo.html', {'ph':ph ,  'photo':photo, 'next':next, 'prev':prev,'len':len1,'id1':a+1})


def consulterfilm (request, id ):
    fm = get_object_or_404(film,id=id)



    return render(request, 'fil.html',{'fm':fm})


def shops(request):

    sh = shop.objects.order_by()

    return render(request, 'shop.html', {'shop':sh})

def consultershop(request, id):

    ph = get_object_or_404(shop,id=id)

    return render(request, 'shopdet.html', {'fm':ph})

def delivery(request):

    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return shops(request)

    else:
        # If the request was not a POST, display the form to enter details.
        form = ClientForm()

    return render(request, 'delivery.html',{'form':form})