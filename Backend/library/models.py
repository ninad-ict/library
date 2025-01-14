from django.db import models


class User(models.Model):
    # Auto-incremented primary key
    id = models.AutoField(primary_key=True)  # Acts as "No."

    # User-specific fields
    user_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    # Role field with predefined choices
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='member'
    )

    # Metadata fields
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email', 'role'], name='unique_email_role')
        ]
    

class BookInventory(models.Model):
    # Auto-incremented primary key
    id = models.AutoField(primary_key=True)  # Acts as "No."

    # Book-specific fields
    book_name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=4, unique=True)  # A 4 digit ISBN number
    author = models.CharField(max_length=255)
    book_cost = models.DecimalField(max_digits=10, decimal_places=2)  
    available_qty = models.PositiveIntegerField()
    publication_date = models.DateField()
    rental_days = models.PositiveIntegerField(default=7)  # Default rental period

    # Metadata fields
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class BookTransaction(models.Model):
    # Auto-incremented primary key
    id = models.AutoField(primary_key=True)  # Acts as "No."

    # Foreign keys to related models
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookInventory, on_delete=models.CASCADE)

    # Transaction details
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_transaction = models.DateField(auto_now_add=True)

    # Status of the transaction
    STATUS_CHOICES = [
        ('taken', 'Taken'),
        ('returned', 'Returned'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='taken')

    # Metadata fields
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
