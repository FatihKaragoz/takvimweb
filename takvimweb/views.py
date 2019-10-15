from takvimweb import eMailAuth
from django.shortcuts import render
from takvim2020.models import menuC,gemici3,gemici1,slider,blog,masaustu,akademik,ajanda,siparis,contact
from django.utils.datastructures import MultiValueDictKeyError

import hashlib

def homeview(request):
    products1 = menuC.objects.filter(menuposition=1)
    products2 = menuC.objects.filter(menuposition=2)
    products11 = ""
    products12 = ""
    produ
    products21 = ""
    products22 = ""
    products23 = ""
    count = 1
    for doc in products1:
        if count == 1:
            products11 = doc
            print(doc.menuItem)
            print("PRODUCT 11")
            print(doc)
        elif count == 2:
            products12 = doc
        elif count==3:
            products13 = doc
        count+=1
    count = 1
    for doc in products2:
        if count==1:
            products21 = doc
        elif count==2:
            products22 = doc
        elif count==3:
            products23 = doc
        count+=1


    sliders = slider.objects.all()
    blogs = blog.objects.all()
    return render(request,'home.html',{'products11':products11,'products12':products12,'products13':products13,'products21':products21,'products22':products22,'products23':products23,'sliders':sliders,'blog':blogs})


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            _email = request.POST['email']
            _password = request.POST['pass']
            print(_email)
            print(_password)
            user = eMailAuth.EmailOrUsernameModelBackend.authenticate(request, username=_email, password=_password)
            if user is not None:
                login(request, user)
                print("################## GİRİŞ YAPILDI")
                return homeview(request)
            else:
                print("Galiba kullaıcı bulunamadı")
                return render(request, 'login.html', {'error': 'yes'})
        else:

            return render(request, 'login.html')
    return render(request, "login.html")


def logon(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            _name = request.POST.get('name')
            _surname = request.POST.get('surname')
            _email = request.POST.get('email')
            _password = request.POST.get('pass')
            _phone = request.POST.get('phone')
            _address = request.POST.get('address')
            _repass = request.POST.get('repass')

            if _name == None and _surname == None and _email == None:
                return  render(request,'logon.html')

            if _name != "" and _surname != "" and _email != "" and _password == _repass:
                m = hashlib.md5(str(_email).encode('utf-8'))
                if eMailAuth.EmailOrUsernameModelBackend.addUser(request, username=m.hexdigest(), email=_email, password=_password,name=_name, surname=_surname, phone=_phone, address=_address) == "OK":
                    print("Kayit basarili")
        else:
            return render(request, 'logon.html')
    else:
        return render(request, 'logon.html')
    return render(request,"logon.html")


def productview(request,productId="all"):
    pieces = ""
    size = ""
    color = ""
    email = ""
    phone = ""
    fullname = ""
    address = ""
    comName = ""
    price = ""
    designService = ""
    orderOkMessage = ""

    if request.method == 'POST':
        pieces = request.POST['num-product']
        if productId == "gemici3" or productId == "gemici1" or productId == "masaustu" or productId=="ajanda":
            size = request.POST['sizeSelection']
            if productId == "gemici3":
                color = request.POST['color']
        price = request.POST['bum-product']
        fullname = request.POST['fullname']

        email = request.POST['email']
        phone = request.POST['phone']
        comName = request.POST['comName']
        address = request.POST['address']

        if productId == "gemici3" or productId == "gemici1" or productId == "masaustu":
            if request.POST['designValue'] == "True":
                designService = "Evet"
            if request.POST['designValue'] == "False":
                designService = "Hayır"

    product  = ""
    if productId == "gemici3":
        product = gemici3.objects.all()
        if request.method == 'POST':
            sipariss = siparis()
            sipariss.pieces = pieces
            sipariss.size = size
            sipariss.fullname = fullname
            sipariss.address = address
            sipariss.phone = phone
            sipariss.email = email
            sipariss.color = color
            sipariss.price = price
            sipariss.sumprice = str(float(price)*float(pieces))
            sipariss.product_id = productId
            sipariss.comName = comName
            sipariss.designService = designService
            try:
                sipariss.design = request.FILES['pic1']
                sipariss.design1 = request.FILES['pic2']
            except MultiValueDictKeyError:
                orderOkMessage = "True"
            sipariss.save()
            orderOkMessage = "True"

    if productId == "gemici1":
        product = gemici1.objects.all()
        if request.method == 'POST':
            sipariss = siparis()
            sipariss.pieces = pieces
            sipariss.fullname = fullname
            sipariss.address = address
            sipariss.phone = phone
            sipariss.email = email
            sipariss.price = price
            sipariss.sumprice = str(float(price)*float(pieces))
            sipariss.product_id = productId
            sipariss.comName = comName
            sipariss.designService = designService
            try:
                sipariss.design = request.FILES['pic1']
                sipariss.design1 = request.FILES['pic2']
            except MultiValueDictKeyError:
                orderOkMessage = "False"
            sipariss.save()
            orderOkMessage = "True"
    if productId == "masaustu":
        product = masaustu.objects.all()
        if request.method == 'POST':
            sipariss = siparis()
            sipariss.pieces = pieces
            sipariss.size = size
            sipariss.fullname = fullname
            sipariss.address = address
            sipariss.phone = phone
            sipariss.email = email
            sipariss.price = price
            sipariss.sumprice = str(float(price)*float(pieces))
            sipariss.product_id = productId
            sipariss.comName = comName
            sipariss.designService = designService
            try:
                sipariss.design = request.FILES['pic1']
                sipariss.design1 = request.FILES['pic2']
            except MultiValueDictKeyError:
                orderOkMessage = "False"
            sipariss.save()
            orderOkMessage = "True"

    if productId == "ajanda":
        product = ajanda.objects.all()
        if request.method == 'POST':
            sipariss = siparis()
            sipariss.pieces = pieces
            sipariss.size = size
            sipariss.fullname = fullname
            sipariss.address = address
            sipariss.phone = phone
            sipariss.email = email
            sipariss.price = price
            sipariss.sumprice = str(float(price) * float(pieces))
            sipariss.product_id = productId
            sipariss.comName = comName
            sipariss.save()
            orderOkMessage = "True"

    if productId == "akademik":
        product = akademik.objects.all()
        if request.method == 'POST':
            product = akademik.objects.all()
            sipariss = siparis()
            sipariss.pieces = pieces
            sipariss.fullname = fullname
            sipariss.address = address
            sipariss.phone = phone
            sipariss.email = email
            sipariss.price = price
            sipariss.sumprice = str(float(price) * float(pieces))
            sipariss.product_id = productId
            sipariss.comName = comName
            sipariss.save()
            orderOkMessage = "True"

    return render(request,"product.html",{'product':product,'orderOkMessage':orderOkMessage})



def blogview(request,blogId="all"):
    blogdetails = ""
    products = menuC.objects.all()
    if blogId != "all":
        blogdetails = blog.objects.filter(blog_id=blogId)
    return render(request,'blog.html',{'blog':blogdetails,'products':products})


def about(request):
    return render(request,'about.html');

def contactview(request):
    if request.method == "POST":
        postContact = contact()
        postContact.fullname = request.POST['fullname']
        postContact.email = request.POST['email']
        postContact.phone = request.POST['phone']
        postContact.message = request.POST['message']
        postContact.message = request.POST['message']
        postContact.save()
    return render(request,'contact.html');


def blogs(request):
    blogs = blog.objects.all()
    return render(request,'blogs.html',{'blogs':blogs})