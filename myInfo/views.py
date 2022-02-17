from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myInfo.models import *
from myInfo.form import *



def info(request):
    return HttpResponse("<H1>Hello</H1>")
def profile(request):
    return render(request, 'profile.html')
def home(request):
    return render(request, 'home2.html')
def Educational(request):
    return render(request, 'Educational.html')
def Interest(request):
    return render(request, 'Interest.html')
def Career(request):
    return render(request, 'Career.html')
def RoleModel(request):
    return render(request, 'RoleModel.html')
def Article(request):
    return render(request, 'Ayticle.html')
def showA1(request):
    return render(request, 'ATC/A1.html')
def showA2(request):
    return render(request, 'ATC/A2.html')
def showA3(request):
    return render(request, 'ATC/A3.html')
def showA4(request):
    return render(request, 'ATC/A4.html')
def showA5(request):
    return render(request, 'ATC/A5.html')
def showA6(request):
    return render(request, 'ATC/A6.html')
def showA7(request):
    return render(request, 'ATC/A7.html')
def showA8(request):
    return render(request, 'ATC/A8.html')
def etc(request):
    return render(request, 'other.html')
def resume(request):
    return render(request, 'resume.html')
def test(request):
    return render(request, 'test.html')
def showMyData(request):
    stdId = '64342310049-8'
    name = 'Phongsak Thiminkul'
    address = '18/05 บ้านหนองแปน ต.บุ่งแก้ว อ.โนนสะอาด จ.อุดรธานี'
    domicile = '18/05 บ้านหนองแปน ต.บุ่งแก้ว อ.โนนสะอาด จ.อุดรธานี'
    gender = 'male'
    weight = '48 กก.'
    height = '168 ซม.'
    color = 'สีแดง'
    food = 'ต้มยำกุ้ง'
    occupation = 'นักเรียนนักศึกษา'
    product = [['Sony A6000', '17900', 'c1.jpg'],
               ['Canon EOS M50', '16000', 'c2.jpg'],
               ['Canon G7X Mark III', '25000', 'c3.jpg'],
               ['OLYMPUS OM-D E-M10 Mark III', '21900', 'c4.jpg'],
               ['Fujifilm X-T100 Kit', '12590', 'c52.jpg'],
               ['FujiFlim X-A5 Kit 15-45 mm', '13890', 'c6.jpg'],
               ['Sony A5100 Kit 16-50 mm', '13990', 'c7.jpg'],
               ['Panasonic Lumix DMC-GF9', '18990', 'c8.jpg'],
               ['Olympus Camera E-PL9', '22990', 'c9.jpg'],
               ['CANON EOS M10', '21990', 'c10.jpg'], ]
    return render(request, 'myLab10.html', {'stdId': stdId, 'name': name, 'address': address, 'domicile': domicile,
                                              'gender': gender, 'weight': weight, 'height': height,
                                              'color': color, 'food': food, 'occupation': occupation,
                                              'product': product, })


def showDataCamera(request):
    dataType = "กล้องถ่ายรูป"
    name = "นายพงษ์ศักดิ์ ทิมิลกุล"
    info = "ถ้าประเภทกล้องเป็น Mirrorless ส่วนลด 10% ถ้าเป็น DSLR ส่วนลด 20% และ compact ไม่มีส่วนลด"
    cameraList = []
    c1 = Camera("001", "Sony", "A6000", "355 G", "Mirrorless", 17900.00)
    c2 = Camera("002", "Leica", "TL2", "355 G", "Mirrorless", 135000.00)
    c3 = Camera("003", "Nikon", "D5600", "500 G", "DSLR", 36431.00)
    c4 = Camera("004", "Cannon", "EOS 800D", "532 G", "DSLR", 14041.00)
    c5 = Camera("005", "Olympus", "OM-D E-M10 Mark III", "363 G", "Mirrorless", 21000.00)
    c6 = Camera("006", "Sony", "ILCE-6300", "361 G", "Mirrorless", 27990.00)
    c7 = Camera("007", "FUJIFILM ", "X-A10", "331 G", "Mirrorless", 19990.00)
    c8 = Camera("008", "Panasonic ", "Lumix DMC-GF9", "269 G", "DSLR", 30000.00)
    c9 = Camera("009", "Canon", "PowerShot SX740 HS", "299 G", "compact", 12590.00)
    c10 = Camera("010", "Sony", "ZV-1", "294 G", "compact", 22990.00)
    c11 = Camera("011", "Canon", "G7X Mark III", "304 G", "compact", 23900.00)
    c12 = Camera("012", "Panasonic", "Lumix TZ220", "340 G", "compact", 24691.00)
    c13 = Camera("013", "Ricoh", "Ricoh GR III", "257 G", "compact", 30900.00)
    c14 = Camera("014", "Sony", "Cyber-shot RX100 VII", "302 G", "compact", 34990.00)
    c15 = Camera("015", "Leica", "D-LUX 7", "392 G", "compact", 38999.00)
    cameraList.append(c1)
    cameraList.append(c2)
    cameraList.append(c3)
    cameraList.append(c4)
    cameraList.append(c5)
    cameraList.append(c6)
    cameraList.append(c7)
    cameraList.append(c8)
    cameraList.append(c9)
    cameraList.append(c10)
    cameraList.append(c11)
    cameraList.append(c12)
    cameraList.append(c13)
    cameraList.append(c14)
    cameraList.append(c15)
    return render(request, 'myLab11.html', {'dataType': dataType,'name': name, 'info': info, 'cameraList': cameraList})

def showGoods(request):
    productList = Goods.objects.all()
    return render(request, 'frmGoods/showGoodsList.html', {'productList': productList})

def showOneGoods(request, gid):
    context = {}
    context['Goods'] = Goods.objects.get(gid=gid)
    return render(request, 'frmGoods/showGoodsOne.html', context)

def newGoods(request):
    if request.method == "POST":
        newForm = ProductFormCreate(request.POST)
        if newForm.is_valid():
            newForm.save()
        return redirect('goods')
    else:
        newForm = ProductFormCreate()
        return render(request, 'frmGoods/newGoods.html', {'form': newForm})

def updateGoods(request, gid):
    obj = get_object_or_404(Goods, gid=gid)
    updateForm = ProductFormUpdate(request.POST or None, instance=obj)
    if request.method == "POST":
        if updateForm.is_valid():
            updateForm.save()
        return redirect('goods')
    else:
        return render(request, "frmGoods/updateGoods.html", {'form': updateForm})

def deleteGoods(request, gid):
    obj = get_object_or_404(Goods, gid=gid)
    if request.method == "POST":
        obj.delete()
        return redirect('goods')
    else:
        return render(request, "frmGoods/delectGoods.html", {'Goods': obj})


def showCustomer(request):
    customerList = Customer.objects.all()
    return render(request, 'frmGoods/showCustomerList.html', {'customerList': customerList})

def showOneCustomer(request, cid):
    context = {}
    context['Customer'] = Customer.objects.get(cid=cid)
    return render(request, 'frmGoods/showCustomerOne.html', context)

def newCustomer(request):
    if request.method == "POST":
        CusnewForm = CustomerFormCreate(request.POST)
        if CusnewForm.is_valid():
            CusnewForm.save()
        return redirect('Customer')
    else:
        CusnewForm = CustomerFormCreate()
        return render(request, 'frmGoods/newCustomer.html', {'form': CusnewForm})

def updateCustomer(request, cid):
    obj = get_object_or_404(Customer, cid=cid)
    CusUpForm = CustomerFormUpdate(request.POST or None, instance=obj)
    if request.method == "POST":
        if CusUpForm.is_valid():
            CusUpForm.save()
        return redirect('Customer')
    else:
        return render(request, "frmGoods/updateCustomer.html", {'form': CusUpForm})

def deleteCustomer(request, cid):
    obj = get_object_or_404(Customer, cid=cid)
    if request.method == "POST":
        obj.delete()
        return redirect('Customer')
    else:
        return render(request, "frmGoods/deleteCustomer.html", {'Customer': obj})