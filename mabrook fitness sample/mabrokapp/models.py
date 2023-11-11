from django.db import models

# Create your models here.


class EquipmentCategory(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(unique=True,max_length=45)
    date_created=models.DateField(auto_now=True)
    class Meta:
        verbose_name_plural="Equipment categories"
    def __str__(self) :
     return self.category_name

class Products(models.Model):
    product_id=models.AutoField(primary_key=True)
    category_id=models.ForeignKey(EquipmentCategory,on_delete=models.CASCADE)
    product_name=models.CharField(unique=True,max_length=45)
    unit_price=models.IntegerField(default=0)
    sales_price=models.IntegerField(default=0)
    unit_measure=models.CharField(max_length=10)
    date_updated=models.DateField(auto_now=True)
    class Meta:
       verbose_name_plural="Products"
    def __str__(self) :
       return self.product_name
class Transactions(models.Model):
   transactions_id=models.AutoField(primary_key=True)
   product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
   transactions_type=models.CharField(max_length=10)
   stock_taken=models.IntegerField(default=0)
   transactions_amount=models.IntegerField(default=0)
   transactions_date=models.DateField(auto_now=True)
   class Meta:
      verbose_name_plural="Transactions"