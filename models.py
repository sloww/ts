from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Address(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        )

    province = models.CharField(
        max_length = 100,
        verbose_name = '省份',
        default = '',
        blank = True,
        )

    city = models.CharField(
        max_length = 100,
        verbose_name = '城市',
        )

    district = models.CharField(
        max_length = 100,
        verbose_name = '区',
        )

    detail = models.CharField(
        max_length = 100,
        verbose_name = '详细',
        )

    class Meta():
        verbose_name = '地址'
        verbose_name_plural = '1.地址'

    def __str__(self):
        return('%s%s %s %s' % (self.province,self.city,self.district,self.detail))

class Company(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        )

    address = models.ForeignKey(
        Address,
        on_delete = models.CASCADE,
        )
    name = models.CharField(
        max_length = 100,
        verbose_name = "单位名称",
        )

    tax_number = models.CharField(
        max_length = 100,
        verbose_name = "企业信用代码",
        blank = True,
        )


    bank_info = models.CharField(
        max_length = 220,
        verbose_name = "银行信息",
        blank = True,
        )

    registered_address = models.CharField(
        max_length = 220,
        verbose_name = "注册地信息",
        blank = True,
        )

    class Meta():
        verbose_name = '公司'
        verbose_name_plural = '2.公司'

    def __str__(self):
        return(self.name)

class Contact(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        )

    company = models.ForeignKey(
        'Company',
        on_delete = models.CASCADE,
        )
        

    name = models.CharField(
        max_length = 100,
        verbose_name = "名称",
        )

    phone = models.CharField(
        max_length = 100,
        verbose_name = "电话",
        )

    class Meta():
        verbose_name = '联系人'
        verbose_name_plural = '3.联系人'
         
    def __str__(self):
        return(self.name)
        
#暂时不使用，先用最简单的用起来         
class Product(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
        )

    name = models.CharField(
        max_length = 100,
        verbose_name = "名称",
        )

    spec = models.CharField(
        max_length = 100,
        verbose_name = '规格',
        )

class Deal(models.Model):
    
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
        )

    num = models.CharField(
        max_length = 100,
        verbose_name = "编号",
        unique = True,
        )

    owner = models.ForeignKey(
        'Contact',
        related_name='Contact_owner',
        on_delete = models.CASCADE,
        verbose_name = '乙方',
        )   

    buyer = models.ForeignKey(
        'Contact',
        related_name='Contact_buyer',
        on_delete = models.CASCADE,
        verbose_name = '甲方',
        )

    total_set = models.DecimalField(
        default = 0,
        verbose_name = '总价',
        max_digits = 20,
        decimal_places =4,
        )

    p1name = models.CharField(
        max_length = 100,
        verbose_name = "名称1",
        )

    p1spec = models.CharField(
        max_length = 100,
        verbose_name = '规格1',
        )

    p1price = models.DecimalField(
        default = 0,
        verbose_name = '价格1',
        max_digits = 20,
        decimal_places =2,
        )

    p1count = models.DecimalField(
        default = 0,
        verbose_name = '数量1',
        max_digits = 20,
        decimal_places =2,
        )

    p2name = models.CharField(
        max_length = 100,
        verbose_name = "名称2",
        blank = True,
        )

    p2spec = models.CharField(
        max_length = 100,
        verbose_name = '规格2',
        blank = True,
        )

    p2price = models.DecimalField(
        default = 0,
        verbose_name = '价格2',
        max_digits = 20,
        decimal_places =2,
        )

    p2count = models.DecimalField(
        default = 0,
        verbose_name = '数量2',
        max_digits = 20,
        decimal_places =2,
        )
    p3name = models.CharField(
        max_length = 100,
        verbose_name = "名称3",
        blank = True,
        )

    p3spec = models.CharField(
        max_length = 100,
        verbose_name = '规格3',
        blank = True,
        )

    p3price = models.DecimalField(
        default = 0,
        verbose_name = '价格3',
        max_digits = 20,
        decimal_places =2,
        )

    p3count = models.DecimalField(
        default = 0,
        verbose_name = '数量3',
        max_digits = 20,
        decimal_places =2,
        )

    show_tax = models.BooleanField(
        default = True,
        verbose_name = '是否显示发票信息',
        )
    
    tax = models.IntegerField(
        default =0,
        verbose_name = '税率',
        )

    signed_date =models.DateField(
        verbose_name = '签订日期',
        default = timezone.now(),
        blank = True,
        )

    delivery_date =models.DateField(
        verbose_name = '期望交货期',
        default = timezone.now(),
        blank = True,
        )


    delivery_add = models.CharField(
        blank = True,
        verbose_name =  '快递地址',
        max_length = 200,
        )

    url = models.UrlField(
        default='https://',
        verbose_name = "URL地址",
        )

 
    class Meta():
        verbose_name = '单据'
        verbose_name_plural = '4.单据'

    def __str__(self):
        return(self.num)

    def total(self):
        return self.p1price*self.p1count + self.p2price*self.p2count + self.p3price*self.p3count

    def p1(self):
        return self.p1price*self.p1count

    def p2(self):
        return self.p2price*self.p2count

    def p3(self):
        return self.p3price*self.p3count

    def owner_company(self):
        return self.owner.company.name 

    def buyer_company(self):
        return self.buyer.company.name 

     def save(self, *args, **kwargs):
        self.url = settings.TSURLPRE+ts/+self.num+'/'
        super(Deal, self).save(*args, **kwargs) 
