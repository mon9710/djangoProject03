
from django.db import models


class Camera :

    def __init__(self, c_id, brand, model, weight,  c_type, price):
        self.__c_id = c_id
        self.__brand = brand
        self.__model = model
        self.__weight = weight
        self.__price = price
        self.__c_type = c_type
        self.__setDiscount()
        self.__setNet()


    def __setDiscount(self):
        if self.__c_type == 'Mirrorless':
            self.__discount = (self.__price * 10)/100
        elif self.__c_type == 'DSLR':
            self.__discount = (self.__price * 20)/100
        elif self.__c_type == 'compact':
            self.__discount = (self.__price * 5) / 100
        else:
            self.__discount = 0

    def __setNet(self):
        self.__net = self.__price - self.__discount

    def getCid(self):
        return self.__c_id

    def getBrand(self):
        return self.__brand

    def getModel(self):
        return self.__model

    def getWeight(self):
        return self.__weight

    def getCType(self):
        return self.__c_type

    def getDiscount(self):
        return self.__discount

    def getNet(self):
        return self.__net

    def getPrice(self):
        return self.__price

class GoodsCategory(models.Model):
    gc_name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=200, default="")

    def __str__(self):
        return 'GoodsCatID :' + str(self.id) + ',GoodsCatName :' + self.gc_name

class Goods(models.Model):
    goodsCategory = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, default=None)
    gid = models.CharField(max_length=13, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    brand = models.CharField(max_length=60, default="")
    model = models.CharField(max_length=60, default="")
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    property = models.CharField(max_length=50, default="")

    def __str__(self):
        return 'GoodsID :' + str(
            self.gid) + ',GoodsName :' + self.name + ',brand :' + self.brand + ',price :' + str(
            self.price) + ',Net :' + str(self.net)

class Customer(models.Model):
    cid = models.CharField(max_length=13, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    telephone = models.CharField(max_length=10, default="")
    gender = models.CharField(max_length=50, default="")
    carreer = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=10, default="")

    def __str__(self):
        return 'CustomerID :' + str(
            self.cid) + ',CustomerName :' + self.name + ',surname :' + self.surname + ',address :' + self.address

class Order(models.Model):
    oid = models.CharField(max_length=13, primary_key=True, default="")
    date = models.CharField(max_length=50, default="")
    cid = models.CharField(max_length=13, default="")
    status = models.CharField(max_length=100, default="")

    def __str__(self):
        return 'OrderID :' + str(
            self.cid) + ',date :' + self.date + ',CustomerID :' + self.cid + ',status :' + self.status

class OrderDetail(models.Model):
    oid = models.CharField(max_length=13, default="")
    gid = models.CharField(max_length=13, default="")
    price = models.FloatField(default=0.00)
    quantity = models.CharField(max_length=100, default="")

    def __str__(self):
        return 'OrderDetailID :' + str(
            self.id) + ', OrderID:' + self.oid + ',GoodsID :' + self.gid + ',price :' + str(self.price)