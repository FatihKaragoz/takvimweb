import uu

from takvimweb import eMailAuth
from django.shortcuts import render
from takvim2020.models import menuC,gemici3,gemici2,gemici1,gemicieko,slider,blog,masaustu,akademik,ajanda,siparis,contact
from django.utils.datastructures import MultiValueDictKeyError
import uuid
import hashlib
import time

def homeview(request):
    menu = menuC.objects.order_by('-ordering')

    products11 = ""
    products12 = ""
    products13 = ""
    products21 = ""
    products22 = ""
    products23 = ""
    count = 1
    for doc in menu:
        if count == 1:
            products11 = doc
        elif count == 2:
            products12 = doc
        elif count == 3:
            products13 = doc
        elif count == 4:
            products21 = doc
        elif count == 5:
            products22 = doc
        count+=1

    sliders = slider.objects.order_by('idd')
    

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
    if productId=="gemici3" or productId=="gemici1" or productId=="gemici2" or productId=="gemicieko":
        size = "32 x 77.5 cm"
    else:
        size = "17 x 24 cm"
    color = "Empty"
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
        # if productId == "gemici3" or productId == "gemici1" or productId == "masaustu" or productId=="ajanda":
            # size = request.POST['sizeSelection']
            # if productId == "gemici3":
            #     color = request.POST['color']
        price = request.POST['bum-product']
        fullname = request.POST['fullname']

        email = request.POST['email']
        phone = request.POST['phone']
        comName = request.POST['comName']
        address = request.POST['address']

        if productId == "gemici3" or productId == "gemici1" or productId == "masaustu" or productId == "gemici2" or productId == "gemicieko":
            if request.POST['designValue'] == "True":
                designService = "Evet"
            if request.POST['designValue'] == "False":
                designService = "Hayır"

    product  = ""
    if productId == "gemici3":
        product = gemici3.objects.all()
        if request.method == 'POST':
            summPrice = float(price)*float(pieces)
            try:
                siparis.objects.create(siparis_id=uuid.uuid4(),pieces=pieces,size=size,fullname=fullname,address=address,phone=phone,email=email,color=color,price=price,sumprice=summPrice,product_id=productId,comName=comName,designService=designService,design=request.FILES['pic1'],design1=request.FILES['pic2'])
            except MultiValueDictKeyError:
                orderOkMessage = "True"
                siparis.objects.create(siparis_id=uuid.uuid4(), pieces=pieces, size=size, fullname=fullname, address=address, phone=phone, email=email, color=color, price=price, sumprice=summPrice, product_id=productId, comName=comName, designService=designService, design1="", design="")
            orderOkMessage = "True"

    if productId == "gemici1":
        product = gemici1.objects.all()
        if request.method == 'POST':
            summPrice = float(price)*float(pieces)
            try:
                siparis.objects.create(siparis_id=uuid.uuid4(), pieces=pieces, size=size, fullname=fullname,
                                       address=address, phone=phone, email=email, color=color, price=price,
                                       sumprice=summPrice, product_id=productId, comName=comName,
                                       designService=designService, design=request.FILES['pic1'],
                                       design1=request.FILES['pic2'])
            except MultiValueDictKeyError:
                orderOkMessage = "False"
                siparis.objects.create(siparis_id=uuid.uuid4(), pieces=pieces, size=size, fullname=fullname, address=address, phone=phone, email=email, color=color, price=price, sumprice=summPrice, product_id=productId, comName=comName, designService=designService, design1="", design="")
            orderOkMessage = "True"

    if productId == "gemici2":
        product = gemici2.objects.all()
        if request.method == 'POST':
            summPrice = float(price)*float(pieces)
            try:
                siparis.objects.create(siparis_id=uuid.uuid4(), pieces=pieces, size=size, fullname=fullname,
                                       address=address, phone=phone, email=email, color=color, price=price,
                                       sumprice=summPrice, product_id=productId, comName=comName,
                                       designService=designService, design=request.FILES['pic1'],
                                       design1=request.FILES['pic2'])
            except MultiValueDictKeyError:
                siparis.objects.create(siparis_id=uuid.uuid4(), pieces=pieces, size=size, fullname=fullname, address=address, phone=phone, email=email, color=color, price=price, sumprice=summPrice, product_id=productId, comName=comName, designService=designService, design1="", design="")
                orderOkMessage = "False"
            orderOkMessage = "True"

    if productId == "gemicieko":
        product = gemicieko.objects.all()
        if request.method == 'POST':
            summPrice = float(price)*float(pieces)
            try:
                siparis.objects.create(siparis_id=uuid.uuid4(), pieces=pieces, size=size, fullname=fullname,
                                       address=address, phone=phone, email=email, color=color, price=price,
                                       sumprice=summPrice, product_id=productId, comName=comName,
                                       designService=designService, design=request.FILES['pic1'])
            except MultiValueDictKeyError:
                siparis.objects.create(siparis_id=uuid.uuid4(), pieces=pieces, size=size, fullname=fullname, address=address, phone=phone, email=email, color=color, price=price, sumprice=summPrice, product_id=productId, comName=comName, designService=designService, design1="", design="")
            orderOkMessage = "True"

    if productId == "masaustu":
        product = masaustu.objects.all()
        if request.method == 'POST':
            summPrice = float(price)*float(pieces)
            try:
                siparis.objects.create(siparis_id=uuid.uuid4(), pieces=pieces, size=size, fullname=fullname,
                                       address=address, phone=phone, email=email, color=color, price=price,
                                       sumprice=summPrice, product_id=productId, comName=comName,
                                       designService=designService, design=request.FILES['pic1'],
                                       design1=request.FILES['pic2'])
            except MultiValueDictKeyError:
                siparis.objects.create(siparis_id=uuid.uuid4(), pieces=pieces, size=size, fullname=fullname, address=address, phone=phone, email=email, color=color, price=price, sumprice=summPrice, product_id=productId, comName=comName, designService=designService, design1="", design="")
            orderOkMessage = "True"

    if productId == "ajanda":
        product = ajanda.objects.all()
        if request.method == 'POST':
            summPrice = float(price)*float(pieces)
            siparis.objects.create(siparis_id=uuid.uuid4(), pieces=pieces, size=size, fullname=fullname,
                                   address=address, phone=phone, email=email, price=price,
                                   sumprice=summPrice, product_id=productId, comName=comName,
                                   designService=designService, design1="", design="")
            orderOkMessage = "True"
    if productId == "akademik":
        product = akademik.objects.all()
        if request.method == 'POST':
            product = akademik.objects.all()
            summPrice = float(price)*float(pieces)
            orderOkMessage = "True"
    return render(request,"product.html",{'product':product,'orderOkMessage':orderOkMessage})

def blogview(request,blogId="all"):
    blogdetails = ""
    products = menuC.objects.all()
    if blogId != "all":
        blogdetails = blog.objects.filter(blog_id=blogId)
    return render(request,'blog.html',{'blog':blogdetails,'products':products})


def about(request):
    return render(request,'about.html')

def contactview(request):
    if request.method == "POST":
        contact.objects.create(fullname=request.POST['fullname'],email=request.POST['email'],phone=request.POST['phone'],message=request.POST['mesaage'])
    return render(request,'contact.html')

def blogs(request):
    blogs = blog.objects.all()
    return render(request,'blogs.html',{'blogs':blogs})
