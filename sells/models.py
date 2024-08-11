from django.db import models
from django.utils import timezone

# Products Table
class Product(models.Model):
    product_name = models.CharField(max_length=255, null=False)
    product_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

# Distributors Table
class Distributor(models.Model):
    distributor_name = models.CharField(max_length=255, null=False)
    contact_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.distributor_name

# Orders Table
class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid')
    ]

    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    total_cost = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    payment_status = models.CharField(max_length=6, choices=PAYMENT_STATUS_CHOICES, default='Unpaid')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.distributor}"

# OrderDetails Table
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, null=False)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.price
        super(OrderDetail, self).save(*args, **kwargs)

    def __str__(self):
        return f"OrderDetail {self.id} - {self.order}"

# Payments Table
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=False)

    def __str__(self):
        return f"Payment {self.id} - {self.order}"

# Expenses Table
class Expense(models.Model):
    expense_description = models.TextField(null=False)
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    expense_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Expense {self.id} - {self.amount}"

# Salaries Table
class Salary(models.Model):
    employee_name = models.CharField(max_length=255, null=False)
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    salary_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Salary {self.id} - {self.employee_name}"

# Employees Table (Optional)
class Employee(models.Model):
    employee_name = models.CharField(max_length=255, null=False)
    position = models.CharField(max_length=255, blank=True, null=True)
    contact_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee_name