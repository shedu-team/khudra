from django.contrib import admin
from .models import (Product, Distributor,
Order, OrderDetail, Payment, Expense, 
Salary, Employee)

# Register your models here.
admin.site.register(Product)
admin.site.register(Distributor)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Payment)
admin.site.register(Expense)
admin.site.register(Salary)
admin.site.register(Employee)