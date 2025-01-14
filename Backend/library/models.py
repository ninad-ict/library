from django.db import models
from django.core.exceptions import ValidationError


class User(models.Model):
    id = models.AutoField(primary_key=True)  
    user_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='member'
    )

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email', 'role'], name='unique_email_role')
        ]
    

class BookInventory(models.Model):
    id = models.AutoField(primary_key=True) 
    book_name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=4, unique=True)  # A 4 digit ISBN number
    author = models.CharField(max_length=255)
    book_cost = models.DecimalField(max_digits=10, decimal_places=2)  
    available_qty = models.PositiveIntegerField()
    publication_date = models.DateField()
    rental_days = models.PositiveIntegerField(default=7)  # Default rental period
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    
class BookTransaction(models.Model):
    id = models.AutoField(primary_key=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookInventory, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_transaction = models.DateField(auto_now_add=True)

    STATUS_CHOICES = [
        ('taken', 'Taken'),
        ('returned', 'Returned'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='taken')

    # Metadata fields
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
